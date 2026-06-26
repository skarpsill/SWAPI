---
title: "ModelDocExtension::IsVirtualComponent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__IsVirtualComponent.htm"
---

# ModelDocExtension::IsVirtualComponent

This method is obsolete and has been superseded
by[ModelDocExtension::IsVirtualComponent2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__IsVirtualComponent2.htm).

Description

This method gets the path
of the parent assembly of a model if the model is a virtual component.

Syntax (OLE Automation)

*ParentPath = ModelDocExtension.IsVirtualComponent
()

(Table)=========================================================

| Output: | (BSTR ) *ParentPath | Fully qualified path of the parent
assembly of a model if the model is a virtual component; otherwise, an
empty string is returned |
| --- | --- | --- |

Syntax (COM)

status = ModelDocExtension->IsVirtualComponent
( &ParentPath)

Parameters Table Start

(Table)=========================================================

| Output: | (BSTR ) *ParentPath | Fully qualified path of the parent
assembly of a model if the model is a virtual component; otherwise, an
empty string is returned |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only works, and
should only be called, if the model document isopened
in its own window.

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
<param name="Items" value="ZReleaseNotes008$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDocExtension\ModelDocExtension__IsVirtualComponent.htm" >
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
<param name="Items" value="ModelDocExtension_Object$$**$$ZGetVirtualComponent$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDocExtension\ModelDocExtension__IsVirtualComponent.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
