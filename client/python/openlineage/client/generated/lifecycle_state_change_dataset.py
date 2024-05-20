# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum
from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel


class LifecycleStateChange(Enum):
    ALTER = "ALTER"
    CREATE = "CREATE"
    DROP = "DROP"
    OVERWRITE = "OVERWRITE"
    RENAME = "RENAME"
    TRUNCATE = "TRUNCATE"


class LifecycleStateChangeDatasetFacet(DatasetFacet):
    lifecycleStateChange: LifecycleStateChange
    """
    The lifecycle state change.
    """
    previousIdentifier: Optional[PreviousIdentifier] = None
    """
    Previous name of the dataset in case of renaming it.
    """


class Model(BaseModel):
    lifecycleStateChange: Optional[LifecycleStateChangeDatasetFacet] = None


class PreviousIdentifier(BaseModel):
    name: str
    namespace: str
