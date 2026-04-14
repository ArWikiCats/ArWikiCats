"""Configuration classes for the resolver chain.

This module provides dataclasses for configuring resolver behavior,
including priority ordering, caching settings, and debug options.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ResolverConfig:
    """Configuration for a single resolver in the chain.

    Attributes:
        name: Unique identifier for this resolver (e.g., "time_patterns", "jobs_resolver").
        priority: Execution order (lower numbers run first).
        enabled: Whether this resolver is active in the chain.
        cache_enabled: Whether to cache results from this resolver.
        cache_size: Maximum number of entries to cache (LRU).
        timeout_ms: Optional timeout in milliseconds (0 = no timeout).
        metadata: Additional resolver-specific configuration.
    """

    name: str
    priority: int
    enabled: bool = True
    cache_enabled: bool = True
    cache_size: int = 10000
    timeout_ms: int = 0
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass
class ResolverChainConfig:
    """Overall configuration for the resolver chain.

    Attributes:
        resolvers: List of resolver configurations in priority order.
        global_cache_enabled: Master switch for all caching.
        global_cache_size: Default cache size for resolvers without explicit size.
        debug_mode: Enable verbose logging and debugging.
        stop_on_first_match: If True, stop chain after first non-empty result.
        fallback_to_legacy: If True, try legacy resolvers if new ones fail.
    """

    resolvers: list[ResolverConfig] = field(default_factory=list)
    global_cache_enabled: bool = True
    global_cache_size: int = 50000
    debug_mode: bool = False
    stop_on_first_match: bool = True
    fallback_to_legacy: bool = True

    def add_resolver(
        self,
        name: str,
        priority: int,
        enabled: bool = True,
        cache_size: int = 10000,
    ) -> ResolverChainConfig:
        """Add a resolver configuration and return self for chaining."""
        self.resolvers.append(
            ResolverConfig(
                name=name,
                priority=priority,
                enabled=enabled,
                cache_size=cache_size,
            )
        )
        return self

    def get_enabled_resolvers(self) -> list[ResolverConfig]:
        """Return list of enabled resolvers sorted by priority."""
        return sorted(
            [r for r in self.resolvers if r.enabled],
            key=lambda r: r.priority,
        )


__all__ = [
    "ResolverConfig",
    "ResolverChainConfig",
]
