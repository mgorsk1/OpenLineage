# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import AnyUrl, BaseModel


class DatasourceDatasetFacet(DatasetFacet):
    name: Optional[str] = None
    uri: Optional[AnyUrl] = None


class Model(BaseModel):
    dataSource: Optional[DatasourceDatasetFacet] = None
