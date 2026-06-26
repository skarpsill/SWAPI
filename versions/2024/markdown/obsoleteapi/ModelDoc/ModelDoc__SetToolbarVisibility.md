---
title: "ModelDoc::SetToolbarVisibility"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetToolbarVisibility.htm"
---

# ModelDoc::SetToolbarVisibility

This method is obsolete
and has been superseded by[ModelDoc2::SetToolbarVisibility](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetToolbarVisibility.htm).

Description

This method sets the visibility of a toolbar.

Syntax (OLE Automation)

void ModelDoc.SetToolbarVisibility(
Toolbar, Visible )

(Table)=========================================================

| Input: | (long) Toolbar | Identifier of toolbar as defined in swToolbar_e |
| --- | --- | --- |
| Input: | (BOOL) Visible | TRUE if the toolbar is to be visible, FALSE if it
is hidden |

Syntax (COM)

status = ModelDoc->SetToolbarVisibility(
Toolbar , Visible)

(Table)=========================================================

| Input: | (long) Toolbar | Identifier of toolbar as defined in swToolbar_e |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Visible | TRUE if the toolbar is to be visible, FALSE if it
is to be hidden |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetToolbarVisibility.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
