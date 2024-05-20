# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import RunFacet
from pydantic import BaseModel


class Error(BaseModel):
    errorMessage: str
    """
    Text representation of extraction error message.
    """
    stackTrace: Optional[str] = None
    """
    Stack trace of extraction error message
    """
    task: Optional[str] = None
    """
    Text representation of task that failed. This can be, for example, SQL statement that parser could not interpret.
    """
    taskNumber: Optional[int] = None
    """
    Order of task (counted from 0).
    """


class ExtractionErrorRunFacet(RunFacet):
    totalTasks: int
    """
    The number of distinguishable tasks in a run that were processed by OpenLineage, whether successfully or not. Those could be, for example, distinct SQL statements.
    """
    failedTasks: int
    """
    The number of distinguishable tasks in a run that were processed not successfully by OpenLineage. Those could be, for example, distinct SQL statements.
    """
    errors: list[Error]


class Model(BaseModel):
    extractionError: Optional[ExtractionErrorRunFacet] = None
