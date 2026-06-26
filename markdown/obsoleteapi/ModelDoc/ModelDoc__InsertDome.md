---
title: "ModelDoc::InsertDome"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertDome.htm"
---

# ModelDoc::InsertDome

This
method is obsolete and has been superseded by[ModelDoc2::InsertDome](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertDome.htm).

Description

This method inserts a dome.

Syntax (OLE Automation)

void ModelDoc.InsertDome ( height,
reverseDir, doEllipticSurface)

(Table)=========================================================

| Input: | (double) height | Height for the dome in meters |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | TRUE if you want to reverse the dome direction, FALSE otherwise |
| Input: | (BOOL) doEllipticSurface | TRUE if you want the dome to be an elliptical surface, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertDome (
height, reverseDir, doEllipticSurface )

(Table)=========================================================

| Input: | (double) height | Hheight for the dome in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | TRUE if you want to reverse the dome direction, FALSE otherwise |
| Input: | (VARIANT_BOOL) doEllipticSurface | TRUE if you want the dome to be an elliptical surface, FALSE otherwise |
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
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZInsertFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertDome.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
