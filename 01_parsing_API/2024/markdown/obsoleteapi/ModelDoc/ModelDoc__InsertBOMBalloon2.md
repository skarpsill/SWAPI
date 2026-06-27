---
title: "ModelDoc::InsertBOMBalloon2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertBOMBalloon2.htm"
---

# ModelDoc::InsertBOMBalloon2

This
method is obsolete and has been superseded by[ModelDoc2::InsertBOMBalloon2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertBOMBalloon2.htm).

Description

This method inserts a BOM balloon based on
the selected object. The selected object can be an edge, silhouette, face,
or vertex.

Syntax (OLE Automation)

retval = ModelDoc.InsertBOMBalloon2 ( style, size,
upperTextStyle, upperText, lowerTextStyle, lowerText )

(Table)=========================================================

| Input: | (long) style | Balloon style as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon Size as
defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Text style for the upper text of the balloon |
| Input: | (BSTR) upperText | Text string to be placed in the upper text of
the balloon |
| Input: | (long) lowerTextStyle | Text style for the lower text of the balloon |
| Input: | (BSTR) lowerText | Text string to be placed in the lower text of
the balloon |
| Return: | (LPDISPATCH) retval | Pointer to the newly created Note object |

Syntax (COM)

status = ModelDoc->IInsertBOMBalloon2 ( style,
size, upperTextStyle, upperText, lowerTextStyle, lowerText, &retval)

(Table)=========================================================

| Input: | (long) style | Balloon style as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon Size as
defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Text style for the upper text of the balloon |
| Input: | (BSTR) upperText | Text string to be placed in the upper text of
the balloon |
| Input: | (long) lowerTextStyle | Text style for the lower text of the balloon |
| Input: | (BSTR) lowerText | Text string to be placed in the lower text of
the balloon |
| Output: | (LPNOTE) retval | Pointer to the newly created Note object |
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertBOMBalloon2.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertBOMBalloon2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
