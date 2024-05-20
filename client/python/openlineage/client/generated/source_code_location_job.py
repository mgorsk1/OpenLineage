# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import JobFacet
from pydantic import AnyUrl, BaseModel, Field
from typing_extensions import Annotated


class Model(BaseModel):
    sourceCodeLocation: Optional[SourceCodeLocationJobFacet] = None


class SourceCodeLocationJobFacet(JobFacet):
    type: Annotated[str, Field(example="git|svn")]
    """
    the source control system
    """
    url: Annotated[
        AnyUrl,
        Field(
            example="https://github.com/MarquezProject/marquez-airflow-quickstart/blob/693e35482bc2e526ced2b5f9f76ef83dec6ec691/dags/dummy_example.py"
        ),
    ]
    """
    the full http URL to locate the file
    """
    repoUrl: Annotated[
        Optional[str],
        Field(
            example="git@github.com:{org}/{repo}.git or https://github.com/{org}/{repo}.git|svn://<your_ip>/<repository_name>"
        ),
    ] = None
    """
    the URL to the repository
    """
    path: Annotated[Optional[str], Field(example="path/to/my/dags")] = None
    """
    the path in the repo containing the source files
    """
    version: Annotated[Optional[str], Field(example="git: the git sha | Svn: the revision number")] = None
    """
    the current version deployed (not a branch name, the actual unique version)
    """
    tag: Optional[str] = None
    """
    optional tag name
    """
    branch: Optional[str] = None
    """
    optional branch name
    """
