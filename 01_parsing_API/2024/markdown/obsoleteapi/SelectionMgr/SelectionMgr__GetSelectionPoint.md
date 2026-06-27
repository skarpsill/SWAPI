---
title: "SelectionMgr::GetSelectionPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectionPoint.htm"
---

# SelectionMgr::GetSelectionPoint

This method is obsolete and has been superseded
by[SelectionMgr::GetSelectionPoint2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectionPoint2.htm).

Description

This
method gets the selected point in model space coordinates from the currently
selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectionPoint
( AtIndex)

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z) |

Syntax (COM)

status = SelectionMgr->IGetSelectionPoint (AtIndex,
retval )

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles, the x,y,z selection point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The point returned from this method cannot lie on the object that was
selected. For example, the end-user can select an edge when the edge is
within the pick radius of their mouse cursor.

However, for face, edge, and vertex selection, you can get a point that
is on the object by using that object's GetClosestPointOn method. To do
this, get the Face2, Edge, or Vertex object using the SelectionMgr::GetSelectedObject5
method, and then use that object to call GetClosestPointOn. Pass the X,Y,Z
values returned from SelectionMgr::GetSelectionPoint, and the GetClosestPointOn
method will return the closest X,Y,Z point that is on the face, edge,
or vertex.

If the selected object is sketch geometry, then the coordinates returned
are in sketch space. The coordinates are 2D and related to the origin
of the sketch that owns the selected geometry.

NOTE:The index starts at 1, even when using C++.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SelectionMgr_Object$$**$$ZGetInfoPoint$$**$$ZGetSelection$$**$$SelectionMgr::SetSelectionPoint$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectionPoint.htm" >
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
<param name="Items" value="Selections_Example$$**$$Get_Selection_Location_Example$$**$$ZoomTo_Example$$**$$EXBOMTableContents$$**$$EXInsertTable$$**$$EXCreateTriadManipulator$$**$$EXEvalutePointOnSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectionPoint.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
