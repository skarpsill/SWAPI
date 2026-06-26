---
title: "DatumOrigin::GetAxisPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DatumOrigin/DatumOrigin__GetAxisPoints.htm"
---

# DatumOrigin::GetAxisPoints

This method is obsolete and has been superseded
by[DatumOrigin::GetAxisPoint2](sldworksAPI.chm::/DatumOrigin/DatumOrigin__GetAxisPoints2.htm).

Description

This method gets the points
that define the geometry of this datum origin.

Syntax (OLE Automation)

retval = DatumOrigin.GetAxisPoints ()

(Table)=========================================================

| Output: | (VARIANT*) retval | VARIANT of type SafeArray of
4 doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = DatumOrigin->IGetAxisPoints ( retval)

Parameters Table Start

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of 4 doubles
(see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method gives the end user control over the
shape of the symbol.

The array of 4 doubles is 2 (X,Y) coordinates in
drawing space:

- The first
  coordinate (array items 0 and 1) is the tip of the arrowhead on the X
  leader portion of the symbol.
- The second
  coordinate (array items 2 and 3) is the tip of the arrowhead on the Y
  leader portion of the symbol.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

The end user has this control via the selection
drag handles of the symbol.

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
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DatumOrigin\DatumOrigin__GetAxisPoints.htm" >
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
<param name="Items" value="DatumOrigin_Object$$**$$DatumOriginAxisPoints$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DatumOrigin\DatumOrigin__GetAxisPoints.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
