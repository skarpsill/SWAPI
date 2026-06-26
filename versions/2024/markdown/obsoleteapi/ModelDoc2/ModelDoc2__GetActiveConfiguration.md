---
title: "ModelDoc2::GetActiveConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetActiveConfiguration.htm"
---

# ModelDoc2::GetActiveConfiguration

This
method is obsolete and has been superseded by ConfigurationManager::ActiveConfiguration .

Description

This method returns the Configuration object currently active for this
document.

NOTE:If this document is an
assembly, then you could use this method to begin your traversal of the
assembly components by making a subsequent call to Configuration::GetRootComponent.

Syntax (OLE Automation)

retval = ModelDoc2.GetActiveConfiguration
( )

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to Dispatch object for the active Configuration object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetActiveConfiguration
( &retval )

(Table)=========================================================

| Output: | (LPCONFIGURATION) retval | Pointer to the active Configuration object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A Component object is based on the currently
active configuration; one assembly configuration might suppress the component,
while another might display it. Therefore, your traversal of Component
objects might vary if you switch to a different configuration.

You should use this method of assembly
traversal to replace previous calls to the Member class.

The order of calls needed in a typical
assembly traversal are:

1. ModelDoc2::GetActiveConfiguration
(called only once)

2. Configuration::GetRootComponent
(called only once)

3. Component2::GetChildren
(called recursively)

Your assembly traversal routine must begin
from the root component and work its way down through the assembly structure.
This is done by recursively calling Component2::GetChildren. Only call
ModelDoc2::GetActiveConfiguration and Configuration::GetRootComponent
once for the entire assembly. In addition, your assembly traversal must
begin with a ModelDoc2 object that has been activated and is visible;
otherwise, the assembly structure may not be intact.

From the SolidWorks API, the Configuration
and Component objects give you access to all the children components,
the component transforms, and the component Body2 objects as seen in a
specific assembly configuration. The Body2 objects and component transforms
may vary based on the configuration; therefore, component traversal should
be done for each of the configurations that exist.

For example, one assembly configuration
might have an assembly-level feature that cuts a hole through each of
the components in the assembly. Using Component2::GetBody on each of the
assembly components returns the body of each component with the hole feature
that was applied in this particular configuration. If you switch to the
configuration without the assembly-level hole and re-traverse the Component
objects, then calling Component2::GetBody for each component returns the
Body object without the hole feature because it was applied in the other
configuration.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__GetActiveConfiguration.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__GetActiveConfiguration.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="EXConfigurations$$**$$Traverse_Assembly_Component_Feature_Example$$**$$EXTraverseAssembly$$**$$EXListConfig$$**$$EXGetAssemblyBoundingBox$$**$$EXTransformAssemblyComponents$$**$$EXMaterialNames$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__GetActiveConfiguration.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
