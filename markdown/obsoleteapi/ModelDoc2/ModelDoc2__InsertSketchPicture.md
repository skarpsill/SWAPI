---
title: "ModelDoc2::InsertSketchPicture"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSketchPicture.htm"
---

# ModelDoc2::InsertSketchPicture

This method is obsolete and has been superseded
by[SketchManager::InsertSketchPicture](sldworksAPI.chm::/SketchManager/SketchManager__InsertSketchPicture.htm).

Description

This method inserts a picture into the current
sketch. Supported image types are:

- Windows
  bitmap (*.bmp)
- Tagged
  Image Format (*.tif)

Syntax (OLE Automation)

pResult = ModelDoc2.InsertSketchPicture ( filename
)

(Table)=========================================================

| Input: | (BSTR) filename | Path to image file including file extension |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) pResult | TRUE if successful, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertSketchPicture ( filename,
&pResult )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) filename | Path to image file including file extension |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) pResult | TRUE if successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__InsertSketchPicture.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
