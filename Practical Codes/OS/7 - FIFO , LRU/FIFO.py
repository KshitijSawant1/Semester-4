def fifo(pages, capacity):
    memory = []
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        print(f"Page: {page} | Memory: {memory}")

    total_requests = len(pages)
    fault_ratio = (page_faults / total_requests)*100
    hit_ratio = (page_hits / total_requests)*100

    print("\nSummary:")
    print(f"Total Page Requests: {total_requests}")
    print(f"Total Page Faults  : {page_faults}")
    print(f"Total Page Hits    : {page_hits}")
    print(f"Page Fault Ratio   : {fault_ratio:.2f}")
    print(f"Page Hit Ratio     : {hit_ratio:.2f}")

# Example usage
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3
fifo(pages, capacity)
