---
title: "Sketch::Autodimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__Autodimension.htm"
---

# Sketch::Autodimension

## Sketch::AutoDimension

This method is obsolete and
has been superseded by[Sketch::AutoDimension2](sldworksAPI.chm::/Sketch/Sketch__AutoDimension2.htm).

Description

This method automatically
dimensions the sketch.

Syntax (OLE Automation)

status = Sketch.AutoDimension ( entitiesToDimension,
horizontalScheme, horizontalPlacement, verticalScheme, verticalPlacement
)

(Table)=========================================================

| Input: | (long) entitiesToDimension | Entities to dimension as defined in swAutodimEntities_e |
| --- | --- | --- |
| Input: | (long) horizontalScheme | Horizontal dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) horizontalPlacement | Placement relative to the sketch of the horizontal dimensions as defined
in swAutodimHorizontalPlacement_e |
| Input: | (long) verticalScheme | Vertical dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) verticalPlacement | Placement relative to the sketch of the vertical dimensions as defined
in swAutodimVerticalPlacement_e |
| Output: | (long) status | swAutodimStatusSuccess if the sketch is automatically dimensioned successfully;
see swAutodimStatus_e for values for possible failures |

Syntax (COM)

status = Sketch->AutoDimension ( entitiesToDimension,
horizontalScheme, horizontalPlacement, verticalScheme, verticalPlacement,
&status )

Parameters Table Start

(Table)=========================================================

| Input: | (long) entitiesToDimension | Entities to dimension as defined in swAutodimEntities_e |
| --- | --- | --- |
| Input: | (long) horizontalScheme | Horizontal dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) horizontalPlacement | Placement relative to the sketch of the horizontal dimensions as defined
in swAutodimHorizontalPlacement_e |
| Input: | (long) verticalScheme | Vertical dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) verticalPlacement | Placement relative to the sketch of the vertical dimensions as defined
in swAutodimVerticalPlacement_e |
| Output: | (long) status | swAutodimStatusSuccess if the sketch is automatically dimensioned successfully;
see swAutodimStatus_e for values for possible failures |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the entitiesToDimension
argument takes the value swAutodimEntitiesSelected, then use ModelDocExtension::SelectByID
with a mark value of swAutodimMarkEntities to select the sketch entities
to dimension.

Select and mark a unique sketch
point or vertical sketch line as the datum for the horizontal dimensioning
scheme, using swAutodimMarkHorizontalDatum as the mark value. Similarly,
select a unique sketch point or horizontal sketch line as the datum for
the vertical dimensioning scheme, using swAutodimMarkVerticalDatum as
the mark value.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Sketch\Sketch__Autodimension.htm" >
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
<param name="Items" value="Sketch_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Sketch\Sketch__Autodimension.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="EXAutoDimensionSketch$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Sketch\Sketch__Autodimension.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
