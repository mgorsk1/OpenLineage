# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Extra, Field
from typing_extensions import Annotated


class BaseEvent(BaseModel):
    eventTime: datetime
    """
    the time the event occurred at
    """
    producer: Annotated[
        AnyUrl, Field(example="https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client")
    ]
    """
    URI identifying the producer of this metadata. For example this could be a git url with a given tag or sha
    """
    schemaURL: Annotated[AnyUrl, Field(example="https://openlineage.io/spec/0-0-1/OpenLineage.json")]
    """
    The JSON Pointer (https://tools.ietf.org/html/rfc6901) URL to the corresponding version of the schema definition for this RunEvent
    """


class BaseFacet(BaseModel):
    class Config:
        extra = Extra.allow

    _producer: Annotated[
        AnyUrl, Field(example="https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client")
    ]
    """
    URI identifying the producer of this metadata. For example this could be a git url with a given tag or sha
    """
    _schemaURL: Annotated[
        AnyUrl, Field(example="https://openlineage.io/spec/1-0-2/OpenLineage.json#/$defs/BaseFacet")
    ]
    """
    The JSON Pointer (https://tools.ietf.org/html/rfc6901) URL to the corresponding version of the schema definition for this facet
    """


class Dataset(BaseModel):
    namespace: Annotated[str, Field(example="my-datasource-namespace")]
    """
    The namespace containing that dataset
    """
    name: Annotated[str, Field(example="instance.schema.table")]
    """
    The unique name for that dataset within that namespace
    """
    facets: Optional[dict[str, DatasetFacet]] = None
    """
    The facets for this dataset
    """


class DatasetEvent(BaseEvent):
    dataset: StaticDataset


class DatasetFacet(BaseFacet):
    _deleted: Optional[bool] = None
    """
    set to true to delete a facet
    """


class EventType(Enum):
    START = "START"
    RUNNING = "RUNNING"
    COMPLETE = "COMPLETE"
    ABORT = "ABORT"
    FAIL = "FAIL"
    OTHER = "OTHER"


class InputDataset(Dataset):
    inputFacets: Optional[dict[str, InputDatasetFacet]] = None
    """
    The input facets for this dataset.
    """


class InputDatasetFacet(BaseFacet):
    pass


class Job(BaseModel):
    namespace: Annotated[str, Field(example="my-scheduler-namespace")]
    """
    The namespace containing that job
    """
    name: Annotated[str, Field(example="myjob.mytask")]
    """
    The unique name for that job within that namespace
    """
    facets: Optional[dict[str, JobFacet]] = None
    """
    The job facets.
    """


class JobEvent(BaseEvent):
    job: Job
    inputs: Optional[list[InputDataset]] = None
    """
    The set of **input** datasets.
    """
    outputs: Optional[list[OutputDataset]] = None
    """
    The set of **output** datasets.
    """


class JobFacet(BaseFacet):
    _deleted: Optional[bool] = None
    """
    set to true to delete a facet
    """


class OutputDataset(Dataset):
    outputFacets: Optional[dict[str, OutputDatasetFacet]] = None
    """
    The output facets for this dataset
    """


class OutputDatasetFacet(BaseFacet):
    pass


class Run(BaseModel):
    runId: UUID
    """
    The globally unique ID of the run associated with the job.
    """
    facets: Optional[dict[str, RunFacet]] = None
    """
    The run facets.
    """


class RunEvent(BaseEvent):
    eventType: Annotated[Optional[EventType], Field(example="START|RUNNING|COMPLETE|ABORT|FAIL|OTHER")] = None
    """
    the current transition of the run state. It is required to issue 1 START event and 1 of [ COMPLETE, ABORT, FAIL ] event per run. Additional events with OTHER eventType can be added to the same run. For example to send additional metadata after the run is complete
    """
    run: Run
    job: Job
    inputs: Optional[list[InputDataset]] = None
    """
    The set of **input** datasets.
    """
    outputs: Optional[list[OutputDataset]] = None
    """
    The set of **output** datasets.
    """


class RunFacet(BaseFacet):
    pass


class StaticDataset(Dataset):
    pass
