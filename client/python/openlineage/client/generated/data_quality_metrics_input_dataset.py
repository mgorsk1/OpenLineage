# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import InputDatasetFacet
from pydantic import BaseModel


class ColumnMetrics(BaseModel):
    nullCount: Optional[int] = None
    """
    The number of null values in this column for the rows evaluated
    """
    distinctCount: Optional[int] = None
    """
    The number of distinct values in this column for the rows evaluated
    """
    sum: Optional[float] = None
    """
    The total sum of values in this column for the rows evaluated
    """
    count: Optional[float] = None
    """
    The number of values in this column
    """
    min: Optional[float] = None
    max: Optional[float] = None
    quantiles: Optional[dict[str, float]] = None
    """
    The property key is the quantile. Examples: 0.1 0.25 0.5 0.75 1
    """


class DataQualityMetricsInputDatasetFacet(InputDatasetFacet):
    rowCount: Optional[int] = None
    """
    The number of rows evaluated
    """
    bytes: Optional[int] = None
    """
    The size in bytes
    """
    fileCount: Optional[int] = None
    """
    The number of files evaluated
    """
    columnMetrics: dict[str, ColumnMetrics]
    """
    The property key is the column name
    """


class Model(BaseModel):
    dataQualityMetrics: Optional[DataQualityMetricsInputDatasetFacet] = None
