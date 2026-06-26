---
title: "ModelDoc::SelectionManager"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectionManager.htm"
---

# ModelDoc::SelectionManager

This property is obsolete
and has been superseded by[ModelDoc2::SelectionManager](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectionManager.htm).

Description

This property makes the current selected object available to the user.
Selection Manager selected objects are transient since they will be invalid
as soon as another selection is made. So these pointers should not be
kept around for long.

Syntax (OLE Automation)

SelectionManager = ModelDoc.SelectionManager (VB
Get property)

SelectionManager = ModelDoc.GetSelectionManager
( ) (C++ Get property)

(Table)=========================================================

| Property: | (LPDISPATCH) SelectionManager | Pointer a Dispatch object, the SelectionMgr object for this document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->get_ISelectionManager(&SelectionMananger)

(Table)=========================================================

| Property: | (LPSELECTIONMGR) SelectionManager | Pointer to the SelectionMgr object for this document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetSelection$$**$$ZGetSelectionMgr$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SelectionManager.htm" >
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
<param name="Items" value="Change_Note_Text_Example$$**$$Fillet_Creation_Example$$**$$Get_Component_Face_By_Name_Example$$**$$Get_Vertex_Example$$**$$Line_from_User_Selection_Example$$**$$Object_Selection_and_Object_Naming_Example$$**$$Selections_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SelectionManager.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
