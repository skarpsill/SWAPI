---
title: "ModelDoc::InsertProtrusionSwept3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertProtrusionSwept3.htm"
---

# ModelDoc::InsertProtrusionSwept3

This method is obsolete and has been superseded by[ModelDoc::InsertProtrusionSwept4](ModelDoc__InsertProtrusionSwept4.htm)

Description

This method inserts a swept boss or base feature from the selected profile
and the selected sweep curves.

Syntax (OLE Automation)

(void) ModelDoc.InsertProtrusionSwept3
( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational,
startMatchingType, endMatchingType )

(Table)=========================================================

| Input: | (Boolean) propagate | If TRUE, then the loft will propagate to the next tangent edge, FALSE
and it will not propagate |
| --- | --- | --- |
| Input: | (Boolean) alignment | If the curve used to sweep goes from one face to another, or from one
edge to another, passing TRUE will cause the sweep to cut completely through
the end faces of the cut; if you choose FALSE, then the swept cut will
begin and end perpendicular to the sweep curve and, therefore, may not
break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (Boolean) keepTangency | If the section curves are tangent, then you have the option to specify
whether the resulting faces will also be tangent; specify TRUE to maintain
the tangency as seen in the section curves, FALSE otherwise; when generating
tangent faces, SolidWorks will maintain planar and cylindrical face shapes
if the section curves exhibit these characteristics |
| Input: | (Boolean) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE
otherwise |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |

Syntax (COM)

status = ModelDoc->InsertProtrusionSwept3
( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational,
startMatchingType, endMatchingType )

(Table)=========================================================

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the loft will propagate to the next tangent edge, FALSE
and it will not propagate |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one
edge to another, passing TRUE will cause the sweep to cut completely through
the end faces of the cut; if you choose FALSE, then the swept cut will
begin and end perpendicular to the sweep curve and, therefore, may not
break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify
whether the resulting faces will also be tangent; specify TRUE to maintain
the tangency as seen in the section curves, FALSE otherwise; when generating
tangent faces, SolidWorks will maintain planar and cylindrical face shapes
if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |
|  |  |  |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use SelectByMark and AndSelectByMarkkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}to
select the profile and sweep curves. The mark for the profile selection
should be a 1; the mark for the sweep path should be 4. If guide curve
selection is provided, then SelectByMark mark should be 2.

ThetwistCtrlOptionargument
can take one of the following values:

- 0 = Follow path
- 1 = Keep constant normal
- 2 = Follow path and
  first guide curve
- 3 = Follow first and
  second guide curve

The tangency type arguments can take the following values:

- 0
  - none
- 1
  - tangent to the normal of the profile
- 2
  - tangent to a selected vector
- 3
  - tangency to all the adjacent faces sharing an edge with the start profile
- 4
  - tangent to some of the selected faces sharing an edge with the start
  profile (not available at this moment)

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertProtrusionSwept3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertProtrusionSwept3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::AndSelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertProtrusionSwept3.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
