---
title: "DrawingDoc::CreateViewport2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateViewport2.htm"
---

# DrawingDoc::CreateViewport2

This method is obsolete and has been superseded
by[DrawingDoc::CreateViewport3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateViewport3.htm).

Description

This
method creates a viewport on a drawing.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateViewport2 ( LowerLeftX, LowerLeftY, UpperRightX, UpperRightY,
sketchSize, scale)

(Table)=========================================================

| Input: | (double)
LowerLeftX | X
value for the lower-left corner of the new viewport |
| --- | --- | --- |
| Input: | (double)
LowerLeftY | Y
value for the lower-left corner of the new viewport |
| Input: | (double)
UpperRightX | X
value for the upper-right corner of the new viewport |
| Input: | (double)
UpperRightY | Y
value for the upper-right corner of the new viewport |
| Input: | (short)
sketchSize | Approximate
number of entities |
| Input: | (double)
scale | Scale
to be used for this viewport |
| Return: | (BSTR)
retval | Name
of the newly created viewport |

Syntax (COM)

status
= DrawingDoc->CreateViewport2 ( LowerLeftX, LowerLeftY, UpperRightX,
UpperRightY, sketchSize, scale, &retval )

(Table)=========================================================

| Input: | (double)
LowerLeftX | X
value for the lower-left corner of the new viewport |
| --- | --- | --- |
| Input: | (double)
LowerLeftY | Y
value for the lower-left corner of the new viewport |
| Input: | (double)
UpperRightX | X
value for the upper-right corner of the new viewport |
| Input: | (double)
UpperRightY | Y
value for the upper-right corner of the new viewport |
| Input: | (short)
sketchSize | Approximate
number of entities |
| Input: | (double)
scale | Scale
to be used for this viewport |
| Output: | (BSTR)
retval | Name
of the newly created viewport |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The default sketchSize value is 0. If you are creating more than 500
sketch entities, specify a value instead of using the default.

After you use this method, you can create sketch entities in the new
viewport. One advantage is that users can move the entities around the
drawing by dragging the viewport instead of selecting all the entities.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateDwgView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateViewport2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
