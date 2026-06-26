---
title: "ModelDoc2::CreatePointDB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePointDB.htm"
---

# ModelDoc2::CreatePointDB

This method is obsolete and has been superseded
by[ModelDoc2::CreatePoint2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePoint2.htm).

IMPORTANT:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
method ignores the z value when adding a point to a 3D sketch. Thus, update
your code to use the more current method, ModelDoc2::CreatePoint2.

Description

This method creates a point.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePointDB ( x, y, z )

(Table)=========================================================

| Input: | (double) x | x coordinate of the point |
| --- | --- | --- |
| Input: | (double) y | y coordinate of the point |
| Input: | (double) z | z coordinate of the point |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc2->CreatePointDB ( x, y, z, &retval
)

Parameters Table Start

(Table)=========================================================

| Input: | (double) x | x coordinate of the point |
| --- | --- | --- |
| Input: | (double) y | y coordinate of the point |
| Input: | (double) z | z coordinate of the point |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__CreatePointDB.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__CreatePointDB.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
