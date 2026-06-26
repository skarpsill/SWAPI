---
title: "SelectionMgr::GetSelectedObjectType2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObjectType2.htm"
---

# SelectionMgr::GetSelectedObjectType2

This
method is obsolete and has been superseded by[SelectionMgr::GetSelectedObjectType3](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectedObjectType3.htm).

Description

This method gets the type of selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObjectType2
( AtIndex)

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (long) retval | Type of object as defined in swSelectType_e |

Syntax (COM)

status = SelectionMgr->GetSelectedObjectType2
( AtIndex, &retval )

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (long) retval | Type of object as defined in swSelectType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The index starts at 1, even when using C++.

When reference surfaces are selected in the graphics
view, this method returns swSelFACES instead of the entireswSelREFSURFACESfeature.

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
<param name="Items" value="SelectionMgr_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObjectType2.htm" >
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
<param name="Items" value="Change_Note_Text_Example$$**$$Fillet_Creation_Example$$**$$Find_Attribute_Example$$**$$Get_Assembly_Component_From_Selected_Entity_Example$$**$$Get_Closest_Point_Example$$**$$Get_Component_Face_By_Name_Example$$**$$Get_Selected_Feature_Example$$**$$Get_Vertex_Example$$**$$Object_Selection_and_Object_Naming_Example$$**$$Selections_Example$$**$$RetrieveExtRef_Example$$**$$Selections_Example$$**$$SectionProperties_Example$$**$$SelectTangentFaces_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObjectType2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
