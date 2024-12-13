import sys


example = "2333133121414131402"
example_small = "12345"


def process(input: str):
    return [int(char) for char in input]


def disk_image(span_sizes):
    image = []
    for file_id, span_idx in enumerate(range(0, len(span_sizes), 2)):
        # Add the file to the image (files are even numbered spans)
        image.extend([file_id for i in range(span_sizes[span_idx])])
        # If this is not the last file, add the next span, which has to be free
        if span_idx + 1 < len(span_sizes):
            # Add the free region to the image
            image.extend([None for _ in range(span_sizes[span_idx + 1])])

    return image


def checksum(image):
    checksum = 0
    for i in range(len(image)):
        if image[i] is not None:
            checksum += i * image[i]
    return checksum


def compact(span_sizes):
    image = disk_image(span_sizes)
    free = -1
    end = len(image)
    while True:
        for idx in range(free + 1, len(image)):
            if image[idx] is None:
                free = idx
                break
        for idx in range(end - 1, 0, -1):
            if image[idx] is not None:
                end = idx
                break
        if free >= end:
            return image
        image[free] = image[end]
        image[end] = None


def find_first_free(image, file_slice):
    file_size = file_slice.stop - file_slice.start
    span = 0
    for i in range(image.index(None), len(image)):
        if i < file_slice.start:
            if image[i] is None:
                span += 1
                if span == file_size:
                    return slice(i + 1 - file_size, i + 1)
            else:
                span = 0
        else:
            return None
    return None


def compact_no_frag(span_sizes):
    image = disk_image(span_sizes)
    files = []
    block_id = 0
    # Scan file boundaries from the back
    for i, span_size in enumerate(span_sizes):
        if i % 2 == 0:
            files.append(slice(block_id, block_id + span_size))
        block_id += span_size
    # We start from the back
    files.reverse()

    for file in files:
        first_free = find_first_free(image, file)
        if first_free is not None:
            image[file], image[first_free] = image[first_free], image[file]
    return image


def part_1(span_sizes):
    compacted_image = compact(span_sizes)
    return checksum(compacted_image)


def part_2(span_sizes):
    compacted_image = compact_no_frag(span_sizes)
    return checksum(compacted_image)


with open("9.in") as f:
    intxt = f.read()

print(f"Day 9 Part 1: {part_1(process(intxt))}")
print(f"Day 9 Part 2: {part_2(process(intxt))}")
