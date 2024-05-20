# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import OutputDatasetFacet
from pydantic import BaseModel


class Model(BaseModel):
    outputStatistics: Optional[OutputStatisticsOutputDatasetFacet] = None


class OutputStatisticsOutputDatasetFacet(OutputDatasetFacet):
    rowCount: Optional[int] = None
    """
    The number of rows written to the dataset
    """
    size: Optional[int] = None
    """
    The size in bytes written to the dataset
    """
    fileCount: Optional[int] = None
    """
    The number of files written to the dataset
    """
