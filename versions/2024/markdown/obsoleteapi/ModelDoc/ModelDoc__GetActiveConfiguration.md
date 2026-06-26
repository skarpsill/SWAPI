---
title: "ModelDoc::GetActiveConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetActiveConfiguration.htm"
---

# ModelDoc::GetActiveConfiguration

This
method is obsolete and has been superseded by[ModelDoc2::GetActiveConfiguration](../ModelDoc2/ModelDoc2__GetActiveConfiguration.htm).

Description

This method returns the currently active Configuration object for this
document. If this document is an assembly, then you can use this method
to begin your traversal of the assembly components by making a subsequent
call to Configuration::GetRootComponent.

Syntax (OLE Automation)

retval = ModelDoc.GetActiveConfiguration
()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to Dispatch object for the active Configuration object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetActiveConfiguration
( &retval )

(Table)=========================================================

| Output: | (LPCONFIGURATION) retval | Pointer to the active Configuration object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A component object is based on the currently
active configuration; one assembly configuration may suppress the component,
while another may display it. Therefore, your traversal of component objects
may vary if you switch to a different configuration.

You should use this method of assembly
traversal to replace previous calls to the Member class.

The
order of calls needed in a typical assembly traversal are:

1. ModelDoc::GetActiveConfiguration
(called only once)

2. Configuration::GetRootComponent
(called only once)

3. Component::GetChildren
(called recursively)

Your assembly traversal routine must begin
from the root component and work its way down through the assembly structure.
This is done by recursively calling Component::GetChildren. Calls to ModelDoc::GetActiveConfiguration
and Configuration::GetRootComponent should only be done once for the entire
assembly. In addition, your assembly traversal must begin with a ModelDoc
object that has been activated and is visible, otherwise, the assembly
structure may not be intact.

From the SolidWorks API, the Configuration
and Component objects access to all the children components, the component
transforms, and the component Body objects as seen in a specific assembly
configuration. The Body objects and component transforms may vary based
on the configuration; therefore, component traversal should be done for
each of the configurations that exist. For example, one assembly configuration
may have an assembly-level feature that cuts a hole through each of the
components in the assembly. Using Component::GetBody on each of the assembly
components will return the body of each component with the hole feature
that was applied in this particular configuration. If you switch to the
configuration without the assembly-level hole and re-traverse the component
objects, then calling Component::GetBody for each component will return
the Body object without the hole feature because it was applied in the
other configuration.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetConfiguration$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc\ModelDoc__GetActiveConfiguration.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Traverse_Assembly_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc\ModelDoc__GetActiveConfiguration.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
