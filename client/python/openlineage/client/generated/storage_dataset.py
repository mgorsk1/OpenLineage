# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel


class Model(BaseModel):
    storage: Optional[StorageDatasetFacet] = None


class StorageDatasetFacet(DatasetFacet):
    storageLayer: str
    """
    Storage layer provider with allowed values: iceberg, delta.
    """
    fileFormat: Optional[str] = None
    """
    File format with allowed values: parquet, orc, avro, json, csv, text, xml.
    """
