---
title: "ModelDoc2::AddDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddDimension.htm"
---

# ModelDoc2::AddDimension

This
method is obsolete and has been superseded by[ModelDoc2::AddDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddDimension2.htm).

Description

This method creates a dimension for the currently selected entities
at the specified location.

Syntax (OLE Automation)

retval = ModelDoc2.AddDimension ( x,
y, z)

(Table)=========================================================

| Input: | (double) x | Dimension text location in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location in meters |
| Input: | (double) z | Dimension text location in meters |
| Return: | (BOOL) retval | 1 = Success, 0 = Failure |

Syntax (COM)

status = ModelDoc2->AddDimension
( x, y, z, &retval )

(Table)=========================================================

| Input: | (double) x | Dimension text location in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location in meters |
| Input: | (double) z | Dimension text location in meters |
| Output: | (VARIANT_BOOL) retval | 1 = Success, 0 = Failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Dimensions are created based on selection location.
For example, creating an angular dimension between two lines gets different
results based on which line endpoints are selected. Therefore, if you
are using ModelDoc2::SelectByID to select the entities for dimensioning,
you should specify the XYZ selection coordinates. You must also leave
the objectName argument empty, because if you pass the objectName argument
to ModelDoc2::SelectByID, then the selection routines tries to locate
that item withoutusing the coordinates.

Because coordinates are ignored when an objectName
is passed, the dimensioning routines are not able to use a specific selection
location for the dimension. This causes unpredictable results in your
dimension creation because you cannot be sure which line endpoint is selected
by the ModelDoc2::SelectByID routine.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__AddDimension.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__AddDimension.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
