---
title: "View::GetDimensionDisplayInfo4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayInfo4.htm"
---

# View::GetDimensionDisplayInfo4

This method is obsolete and has been superseded
by[View::GetDimensionDisplayInfo5](sldworksAPI.chm::/View/View__GetDimensionDisplayInfo5.htm).

Description

This method returns the dimensions in the current
drawing view.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayInfo4 ( )

(Table)=========================================================

| Output: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionDisplayInfo4 ( ArraySize,
retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) ArraySize | Number of items in the array |
| --- | --- | --- |
| Output: | (double*) retval | Array of dimensions of size ArraySize (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For COM implementation, use View::GetDimensionDisplayInfoSize
to determine the size of the array needed to contain the data returned
by this method.

The data returned is an array of doubles as follows:

dimensionCount,[lineCount,[lineSegmentCount[StartPt[3],endPt[3]] ],arcCount,[arcSegmentCount,[arcCenter[3], [StartPt[3],EndPt[3]]
],arrowCount,[arrowTipPt[3],arrowVector[3],arrowWidth,arrowHeight],tolType,isDual,showParens,textAngle,
value1Pos[3],tolmax1Pos[3],tolmin1Pos[3],value2Pos[3],tolmax2Pos[3],tolmin2Pos[3],prefixPos[3],suffixPos[3],tolbox1Corner1[3],tolbox1Corner2[3],tolbox2Corner1[3],tolbox2Corner2[3],parenArc1Start[3],parenArc1End[3],parenArc1Center[3],parenArc1Vector[3],parenArc2Start[3],parenArc2End[3],parenArc2Center[3],parenArc2Vector[3],callout1TextPos[3],callout2TextPos[3]]

where:

dimensionCount= the number of dimensions found in the drawing view

For each dimension, we have the following
data:

lineCount=
the number of extension and leader lines for this dimension

For each line, we have the following data:

StartPt[3] =
an array of three doubles representing the line start point

EndPt[3] =
an array of three doubles representing the line end point

…Repeating theStartPt[3] andEndPt[3]
pair up tolineSegmentCount

arcCount=
the number of leader lines which are arcs for this dimension

For each arc, we have the following data:

arcCenter[3] =
an array of three doubles representing the arc center point

StartPt[3] =
an array of three doubles representing the arc start point

EndPt[3] =
an array of three doubles representing the arc end point

…Repeating thearcCenter[3],StartPt[3],
andEndPt[3] group up toarcSegmentCount

arrowCount=
the number of arrowheads for this dimension

arrowTipPt[3] =
an array of three doubles representing the arrowhead tip location

arrowVector[3] =
an array of three doubles representing the arrow direction

arrowWidth=
the arrowhead width

arrowHeight=
the arrowhead height

…Repeating thearrowTipPt[3],arrowVector[3],arrowWidthandarrowHeightgroup up toarrowCountarrowheads

tolType=
Tolerance type as defined in swTolType_e

isDual=
TRUE if this dimension is a dual dimension, FALSE otherwise

showParens=
TRUE if parenthesis are shown, FALSE otherwise

The next 25 values represent text angle and
positioning. All text positions are the upperleft corner of the string.

textAngle=
text angle in radians (counter clockwise from +ve x-axis)

value1Pos[3] =
XYZ postion of text 1. The position is the upperleft corner of the actual
string.

tolmax1Pos[3] =
XYZ position of max tolerance text 1.

tolmin1Pos[3]
= XYZ position of min tolerance text 1.

value2Pos[3] =
XYZ position of text 2. Data returned is only valid ifisDualis TRUE

tolmax2Pos[3]
= XYZ position of max tolerance text 2. Data returned is valid whenisDualis TRUE

tolmin2Pos[3]
= XYZ position of min tolerance text 2. Data returned is valid whenisDualis TRUE

prefixPos[3] =
XYZ position of prefix text.

suffixPos[3] =
XYZ position of suffix text.

The next 12 values represent the box corners
for dimensions with swTolBASIC tolerance types:

tolbox1Corner1[3] =
XYZ corner 1 of tolerance box 1

tolbox1Corner2[3] =
XYZ corner 2 of tolerance box 1

tolbox2Corner1[3] =
XYZ corner 1 of tolerance box 2. Data returned is valid whenisDualis TRUE

tolbox2corner2[3]
= XYZ corner 2 of tolerance box 2. Data returned is valid whenisDualis TRUE

The next 24 values are valid whenshowParensis TRUE (i.e. - when this is a reference dimension)

parenArc1Start[3] =
XYZ start point of the arc representing parenthesis 1

parenArc1End[3]
= XYZ end point of the arc representing parenthesis 1

parenArc1Center[3]
= XYZ center point of the arc representing parenthesis 1

parenArc1Vector[3]
= XYZ reference direction for the arc representing parenthesis 1

parenArc2Start[3]
= XYZ start point of the arc representing parenthesis 2

parenArc2End[3]
= XYZ end point of the arc representing parenthesis 2

parenArc2Center[3]
= XYZ center point of the arc representing parenthesis 2

parenArc2Vector[3]
= XYZ reference direction for the arc representing parenthesis 2

callout1TextPos[3] =
XYZ position of first callout text (text above)

callout2TextPos[3] =
XYZ position of second callout text (text below)

…Repeating the
entirelineCount … callout2TextPosgroup up todimensionCountdimensions

For example, if a particular view had two dimensions, and the first
dimension had three lines, zero arcs, and two arrows, and the second dimension
had two lines, one arc, and two arrows, then array returned would be as
follows:

[2,3, line1StartPtx,
y, z, line1EndPtx, y, z, line2StartPtx, y, z, line2EndPtx, y, z, line3StartPtx,
y, z, line3EndPtx, y, z,0,2,
arrow1TipPtx, y, z, arrow1Vectorx, y, z, arrow1Width, arrow1Height, arrow2TipPtx,
y, z, arrow2Vectorx, y, z, arrow2Width, arrow2Height, tolType, isDual,
showParens, textAngle, value1Posx, y, z, tolmax1Posx, y, z, tolmin1Posx,
y, z, value2Posx, y, z, tolmax2Posx, y, z, tolmin2Posx, y, z, prefixPosx,
y, z, suffixPosx, y, z, tolbox1Corner1x, y, z, tolbox1Corner2x, y, z,
tolbox2Corner1x, y, z, tolbox2Corner2x, y, z, parenArc1Startx, y, z, parenArc1Endx,
y, z, parenArc1Centerx, y, z, parenArc1Vectorx, y, z, parenArc2Startx,
y, z, parenArc2Endx, y, z, parenArc2Centerx, y, z, parenArc2Vectorx, y,
z, callout1TextPosx, y, z, callout2TextPosx, y, z,2,line1StartPtx, y, z, line1EndPtx, y, z, line2StartPtx, y, z, line2EndPtx,
y, z,1, arc1Vertexx,
y, z, arc1StartPtx, y, z, arc1EndPtx, y, z,2,
arrow1TipPtx, y, z, arrow1Vectorx, y, z, arrow1Width, arrow1Height, arrow2TipPtx,
y, z, arrow2Vectorx, y, z, arrow2Width, arrow2Height, tolType, isDual,
showParens, textAngle, value1Posx, y, z, tolmax1Posx, y, z, tolmin1Posx,
y, z, value2Posx, y, z, tolmax2Posx, y, z, tolmin2Posx, y, z, prefixPosx,
y, z, suffixPosx, y, z, tolbox1Corner1x, y, z, tolbox1Corner2x, y, z,
tolbox2Corner1x, y, z, tolbox2Corner2x, y, z, parenArc1Startx, y, z, parenArc1Endx,
y, z, parenArc1Centerx, y, z, parenArc1Vectorx,y, z, parenArc2Startx, y, z, parenArc2Endx, y, z, parenArc2Centerx, y,
z, parenArc2Vectorx, y, z, callout1TextPosx, y, z, callout2TextPosx, y,
z]

where the3,
0,2and2,1,2represent the number of lines, arcs and arrows for each of the two dimensions.
The information for the second dimension is underlined to distinguish
it from information returned for the first dimension.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionDisplayInfo4.htm" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="View_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionDisplayInfo4.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
