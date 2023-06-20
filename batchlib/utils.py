from typing import List

from batchlib.const import MAX_BATCH_LEN, MAX_BATCH_SIZE, MAX_RECORD_SIZE


def create_output_records(records: List[str]) -> List[List[str]]:
    output_records: List[List[str]] = []
    output_batch: List[str] = []
    curr_batch_size: int = 0
    for record in records:
        if len(record) > MAX_RECORD_SIZE:
            continue
        if len(output_batch) >= MAX_BATCH_LEN or curr_batch_size >= MAX_BATCH_SIZE:
            output_records.append(output_batch)
            output_batch = []
            curr_batch_size = 0
        curr_batch_size += len(record)
        output_batch.append(record)
    if records and output_batch:
        output_records.append(output_batch)
    return output_records
