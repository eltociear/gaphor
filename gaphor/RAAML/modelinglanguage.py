"""The RAAML Modeling Language module is the entrypoint for RAAML related
assets."""

import gaphor.SysML.propertypages  # noqa
from gaphor.abc import ModelingLanguage
from gaphor.core import gettext
from gaphor.diagram.diagramtoolbox import ToolboxDefinition
from gaphor.RAAML.toolbox import raaml_toolbox_actions
from gaphor.SysML import diagramitems, sysml


class RAAMLModelingLanguage(ModelingLanguage):
    @property
    def name(self) -> str:
        return gettext("RAAML")

    @property
    def toolbox_definition(self) -> ToolboxDefinition:
        return raaml_toolbox_actions

    def lookup_element(self, name):
        return getattr(sysml, name, None)

    def lookup_diagram_item(self, name):
        return getattr(diagramitems, name, None)
