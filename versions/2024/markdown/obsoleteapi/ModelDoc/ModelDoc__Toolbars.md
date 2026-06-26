---
title: "ModelDoc::Toolbars"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Toolbars.htm"
---

# ModelDoc::Toolbars

This
method is obsolete and has been superseded by[ModelDoc2::Toolbars](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Toolbars.htm).

Description

This method turns the main SolidWorks toolbars on and off.

Syntax (OLE Automation)

void ModelDoc.Toolbars ( m, vw, skMain,
sk, feat, constr, macro)

(Table)=========================================================

| Input: | (BOOL) m | TRUE for main toolbar on, FALSE for off |
| --- | --- | --- |
| Input: | (BOOL) vw | TRUE for view manipulation toolbar on, FALSE for off |
| Input: | (BOOL) skMain | TRUE for main sketch toolbar on, FALSE for off |
| Input: | (BOOL) sk | TRUE for sketch entity toolbar on, FALSE for off |
| Input: | (BOOL) feat | TRUE for feature toolbar on, FALSE for off |
| Input: | (BOOL) constr | TRUE for relationships toolbar on, FALSE for off |
| Input: | (BOOL) macro | TRUE for macro toolbar on, FALSE for off |

Syntax (COM)

status = ModelDoc->Toolbars ( m,
vw, skMain, sk, feat, constr, macro )

(Table)=========================================================

| Input: | (VARIANT_BOOL) m | TRUE for main toolbar on, FALSE for off |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) vw | TRUE for view manipulation toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) skMain | TRUE for main sketch toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) sk | TRUE for sketch entity toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) feat | TRUE for feature toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) constr | TRUE for relationships toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) macro | TRUE for macro toolbar on, FALSE for off |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See ModelDoc.SetToolbarVisibility for control of all SolidWorks toolbars.

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__Toolbars.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
