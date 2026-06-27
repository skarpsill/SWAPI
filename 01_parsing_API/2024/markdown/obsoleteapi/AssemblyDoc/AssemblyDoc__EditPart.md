---
title: "AssemblyDoc::EditPart"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__EditPart.htm"
---

# AssemblyDoc::EditPart

This method is obsolete and has been superseded by[AssemblyDoc::EditPart2](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__EditPart2.htm).

Description

This method allows you to edit the selected
part within the context of an assembly.

Syntax (OLE Automation)

void AssemblyDoc.EditPart ()

Syntax (COM)

status = AssemblyDoc->EditPart (
)

(Table)=========================================================

| Return: | (HRESULT)status | S_OK if successful |
| --- | --- | --- |

Remarks

To switch back to editing the assembly, see AssemblyDoc::EditAssembly.

When performing an in-context edit of a component,
you can use AssemblyDoc::GetEditTarget to get the ModelDoc object of the
component being edited and to determine which assembly component is being
edited in context. In general, you should not use the ModelDoc object
returned from AssemblyDoc::GetEditTarget to create features within the
component part. Likewise, you should not use the Component2::GetModelDoc
return value to create features in the component being edited in context.

Feature creation (ModelDoc2::CreatePlaneAtOffset3)
typically requires the ModelDoc of the active document. When a component
is being edited in-context, the assembly document is still the active
document. During feature creation, SolidWorks automatically determines
whether the feature should be created and owned by the active assembly,
or if it is an in-context edit in which the feature should be created
and owned by the component part. When you are calling typical feature
creation routines in this situation, use the ModelDoc object of the active
assembly.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDoc\AssemblyDoc__EditPart.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
