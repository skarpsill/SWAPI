---
title: "SelectionMgr::GetSelectedObject5"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObject5.htm"
---

# SelectionMgr::GetSelectedObject5

This method is obsolete and has been superseded
by[SelectionMgr::GetSelectedObject6](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectedObject6.htm).

Description

This method gets the selected
object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObject5 ( AtIndex
)

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items, where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPDISPATCH) retval | Pointer to the Dispatch object as defined in swSelectType_e; NULL may
be returned if type is not supported or if nothing is selected |

Syntax (COM)

status = SelectionMgr->GetSelectedObject5 ( AtIndex,
&retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) AtIndex | Index position with in the current list of selected items, where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPDISPATCH) retval | Pointer to the Dispatch object as defined in swSelectType_e; NULL may
be returned if type is not supported or if nothing is selected |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

(Table)=========================================================

| If... | Then this method returns... |
| --- | --- |
| Reference surfaces are selected in the graphics view | Reference surface faces instead of the entire reference surface feature |
| Dimensions are selected in the graphics view | DisplayDimension object instead of the Dimension object |
| SelectionMgr object obtained from a drawing document | Selected DrawingComponent object |
| SelectionMgr object obtained from a part or assembly document | Component2 object |

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
<param name="Items" value="ZReleaseNotes2003plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject5.htm" >
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
<param name="Items" value="SelectionMgr_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject5.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="MassProperty_Example$$**$$SketchPlane$$**$$SectionProperties_Example$$**$$EXGetSelectedObject$$**$$Selections_Example$$**$$RetrieveExtRef_Example$$**$$EXUseSafeEntity$$**$$EXCalcClosestDistanceFaces$$**$$EXFindLengthSketchSegments$$**$$EXGetConstraints$$**$$EXGetParentFeatures$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject5.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
