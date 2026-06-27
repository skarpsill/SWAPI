---
title: "SelectionMgr::GetSelectedObjectsComponent2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObjectsComponent2.htm"
---

# SelectionMgr::GetSelectedObjectsComponent2

This method is obsolete and has been superseded
by[SelectionMgr::GetSelectedObjectsComponent3](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectedObjectsComponent3.htm).

Description

This method gets the component
of the selected object in assembly mode.

Syntax (OLE Automation)

component = SelectionMgr.GetSelectedObjectsComponent2
( atIndex )

(Table)=========================================================

| Input: | (long) atIndex | Index position with in the current list of selected items, where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPDISPATCH) component | Pointer to the Dispatch object for the selected object (see Remarks ) |

Syntax (COM)

status = SelectionMgr->IGetSelectedObjectsComponent2
( atIndex, &component )

Parameters Table Start

(Table)=========================================================

| Input: | (long) atIndex | Index position with in the current list of selected items, where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPCOMPONENT2) component | Pointer to the selected object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

(Table)=========================================================

| If SelectionMgr object obtained from... | Then this method returns... |
| --- | --- |
| Assembly document | Component2 object For example, if a face on a component in the assembly is selected, then
the component that contains that face is returned. |
| Drawing document | Selected DrawingComponent object |
| Part document | NULL |

NOTE:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The index
starts a 1, even when using C++.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObjectsComponent2.htm" >
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
<param name="Items" value="SelectionMgr_Object$$**$$ZGetSelection$$**$$ZGetSelectionMgr$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObjectsComponent2.htm" >
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
<param name="Items" value="Selections_Example$$**$$RetrieveExtRef_Example$$**$$EXRotateAssemblyComponent$$**$$EXToolsCheckInterference$$**$$EXCombineAssemblyComponentsPart$$**$$EXPartComponentEntity$$**$$EXGetSectionedBodies$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObjectsComponent2.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
