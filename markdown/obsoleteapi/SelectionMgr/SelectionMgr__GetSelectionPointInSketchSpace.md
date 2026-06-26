---
title: "SelectionMgr::GetSelectionPointInSketchSpace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectionPointInSketchSpace.htm"
---

# SelectionMgr::GetSelectionPointInSketchSpace

This method is obsolete and has been superseded
by[SelectionMgr::GetSelectionPointInSketchSpace2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectionPointInSketchSpace2.htm).

Description

This method gets the selection point projected onto the active sketch
and returned in sketch space. The selection point is projected onto the
currently active sketch, resulting in a Z value, which is always 0.00.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectionPointInSketchSpace
( AtIndex)

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z) |

Syntax (COM)

status = SelectionMgr->IGetSelectionPointInSketchSpace
( AtIndex, retval )

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles, the X,Y,Z selection point |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If a sketch is not currently active, then the return value is the same
as that returned by SelectionMgr::GetSelectionPoint.You can determine if a sketch is active by checking for a NULL return
value from ModelDoc2::GetActiveSketch2. In Visual Basic, check for Nothing.
For example:

If (Part.GetActiveSketch
Is Nothing) Then

swApp.SendMsgToUser "No
Active sketch" ' No sketch is active

End If

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
<param name="Items" value="SelectionMgr_Object$$**$$ZGetInfoPoint$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectionPointInSketchSpace.htm" >
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
<param name="Items" value="Selections_Example$$**$$Line_From_User_Selection_Example$$**$$EXTransformSketchModelSpace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectionPointInSketchSpace.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
