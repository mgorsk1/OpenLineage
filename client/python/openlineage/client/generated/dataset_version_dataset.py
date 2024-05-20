# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel


class DatasetVersionDatasetFacet(DatasetFacet):
    datasetVersion: str
    """
    The version of the dataset.
    """


class Model(BaseModel):
    version: Optional[DatasetVersionDatasetFacet] = None
