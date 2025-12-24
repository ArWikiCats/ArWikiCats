#!/usr/bin/env python3
"""
Performance benchmark script to measure ArWikiCats processing speed.

This script benchmarks:
1. Import time
2. First call (with initialization)
3. Cached calls (with LRU cache)
4. Batch processing
"""

import time
from typing import List


def benchmark_import() -> float:
    """Measure import time."""
    start = time.time()
    from ArWikiCats import resolve_arabic_category_label  # noqa: F401
    return time.time() - start


def benchmark_single_category() -> tuple[float, float]:
    """Benchmark single category processing."""
    from ArWikiCats import resolve_arabic_category_label
    
    test_category = "Category:2015 in Yemen"
    
    # First call (may trigger initialization)
    start = time.time()
    result = resolve_arabic_category_label(test_category)
    first_call_time = time.time() - start
    
    # Second call (should be cached)
    start = time.time()
    result = resolve_arabic_category_label(test_category)
    cached_call_time = time.time() - start
    
    return first_call_time, cached_call_time


def benchmark_batch_processing(num_categories: int = 100) -> tuple[float, float]:
    """Benchmark batch processing."""
    from ArWikiCats import batch_resolve_labels
    
    # Create a diverse set of test categories
    base_categories = [
        "Category:2015 in Yemen",
        "Category:Belgian cyclists",
        "Category:1999 establishments in Europe",
        "Category:American television",
        "Category:French footballers",
        "Category:German writers",
        "Category:Italian actors",
        "Category:Spanish musicians",
        "Category:British politicians",
        "Category:Japanese artists",
    ]
    
    # Replicate to reach desired number
    categories = (base_categories * (num_categories // len(base_categories) + 1))[:num_categories]
    
    start = time.time()
    result = batch_resolve_labels(categories)
    total_time = time.time() - start
    
    avg_time = total_time / num_categories
    
    return total_time, avg_time


def main():
    """Run all benchmarks and display results."""
    print("=" * 70)
    print("ArWikiCats Performance Benchmark")
    print("=" * 70)
    
    # Import benchmark
    print("\n1. Import Time")
    print("-" * 70)
    import_time = benchmark_import()
    print(f"   Import time: {import_time:.4f}s")
    
    # Single category benchmark
    print("\n2. Single Category Processing")
    print("-" * 70)
    first_call, cached_call = benchmark_single_category()
    print(f"   First call:        {first_call:.4f}s")
    print(f"   Cached call:       {cached_call:.6f}s")
    print(f"   Speedup:           {first_call / cached_call:.0f}x")
    
    # Batch processing benchmark
    print("\n3. Batch Processing (100 categories)")
    print("-" * 70)
    total_time, avg_time = benchmark_batch_processing(100)
    print(f"   Total time:        {total_time:.4f}s")
    print(f"   Average per cat:   {avg_time * 1000:.2f}ms")
    print(f"   Throughput:        {100 / total_time:.0f} categories/second")
    
    # Larger batch
    print("\n4. Batch Processing (1000 categories)")
    print("-" * 70)
    total_time, avg_time = benchmark_batch_processing(1000)
    print(f"   Total time:        {total_time:.4f}s")
    print(f"   Average per cat:   {avg_time * 1000:.2f}ms")
    print(f"   Throughput:        {1000 / total_time:.0f} categories/second")
    
    print("\n" + "=" * 70)
    print("Benchmark complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
