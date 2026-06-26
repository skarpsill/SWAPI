---
title: "DrawingDoc::AutoBalloon"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AutoBalloon.htm"
---

# DrawingDoc::AutoBalloon

This method is obsolete and has been superseded
by[DrawingDoc::AutoBalloon2](DrawingDoc__AutoBalloon2.htm).

Description

This method automatically
inserts balloons in this drawing view.

Syntax (OLE Automation)

retval = DrawingDoc.AutoBalloon ( Layout)

(Table)=========================================================

| Input: | (long) Layout | Layout style of the balloons
as defined by swBalloonLayoutType_e |
| --- | --- | --- |
| Output: | (VARIANT) retval | Array of Dispatch pointers of
the notes created |

Syntax (COM)

status = DrawingDoc->AutoBalloon ( Layout, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (long) Layout | Layout style of the balloons
as defined by swBalloonLayoutType_e |
| --- | --- | --- |
| Output: | (VARIANT) retval | Array of Dispatch pointers of the notes created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method automatically creates the BOM balloons
for the selected drawing views. If a drawing sheet is selected, then all
of the views in that sheet will have BOM balloons automatically created.

The Layout argument indicates how to initially
lay out the balloons as defined by a value in swBalloonLayoutType_e. It
provides options for laying out the balloons in a box or circle around
the drawing view, or lined up along any of the edges of the drawing view.
If this value is passed in as -1, then that indicates that the document
default layout style should be used. To get or set that default value,
use the ModelDoc2::GetUserPreferenceIntegerValue (swDetailingAutoBallonLayout)
or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingAutoBalloonLayout).

The balloon style follows the document defaults
for single balloon style and balloon text.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}You
can get and set balloon style and balloon using these APIs:

- ModelDoc2::GetUserPreferenceIntegerValue
  or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMBalloonStyle)
- ModelDoc2::GetUserPreferenceIntegerValue
  or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMBalloonFit)
- ModelDoc2::GetUserPreferenceIntegerValue
  or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMUpperText)
- ModelDoc2::GetUserPreferenceIntegerValue
  or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMLowerText)

This method also lets you get only the balloons
just created.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__AutoBalloon.htm" >
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
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__AutoBalloon.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
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
<param name="Items" value="EXInsertAutoballoons$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__AutoBalloon.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
