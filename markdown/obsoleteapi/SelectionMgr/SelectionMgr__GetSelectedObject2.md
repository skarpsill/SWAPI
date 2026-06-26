---
title: "SelectionMgr::GetSelectedObject2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObject2.htm"
---

# SelectionMgr::GetSelectedObject2

This method is obsolete and has been superseded by[SelectionMgr::GetSelectedObject3](SelectionMgr_GetSelectedObject3.htm)

Description

This method gets an interface to the currently selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObject2
( AtIndex)

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object as specified in Remarks or return NULL if type
is not supported |

Syntax (COM)

status = SelectionMgr->IGetSelectedObject2
( AtIndex, &retval )

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPUNKNOWN) retval | Pointer to the Dispatch object as specified in Remarks or return NULL
if type is not supported |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The list below shows the type selected and the object returned by this
method. This method works for the following types:

(Table)=========================================================

| Type Selected | Object Returned |
| --- | --- |
| swSelCOMPONENTS | Component |
| swSelDIMENSIONS | Dimension |
| swSelEDGES | Edge |
| swSelREFEDGES | Edge |
| swSelFACES | Face |
| swSelGTOLS | Gtol |
| swSelNOTES | Note |
| swSelSHEETS | Sheet |
| swSelVERTICES | Vertex |
| swSelDRAWINGVIEWS | View |
| swSelATTRIBUTES | Feature (see NOTE ) |
| swSelBODYFEATURES | Feature (see NOTE ) |
| swSelDATUMAXES | Feature (see NOTE ) |
| swSelDATUMPLANES | Feature (see NOTE ) |
| swSelDATUMPOINTS | Feature (see NOTE ) |
| swSelMATES | Feature (see NOTE ) |
| swSelREFCURVES | Feature (see NOTE ) |
| swSelREFERENCECURVES | Feature (see NOTE ) |
| swSelREFSURFACES | Feature (see NOTE ) |
| swSelSKETCHES | Feature (see NOTE ) |
| NOTE: If Object Returned is a Feature object,
then you must use Feature::GetSpecificFeature to get a more specific object
interface. For example, if the selected object is a Sketch, then this
method returns a Feature object. If you need the Sketch interface, then
you must call the Feature::GetSpecificFeature method to return the Sketch
object. |  |

Not
Supported

- swSelOLEITEMS
- swSelSKETCHSEGS
- swSelSKETCHPOINTS
- swSelSECTIONLINES
- swSelDETAILCIRCLES
- swSelSECTIONTEXT
- swSelEXTSKETCHSEGS
- swSelEXTSKETCHPOINTS
- swSelCENTERMARKS

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
<param name="Items" value="SelectionMgr_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject2.htm" >
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
<param name="Items" value="Selections_Example$$**$$Object_Selection_and_Object_Naming_Example$$**$$Get_Vertex_Example$$**$$Change_Note_Text_Example$$**$$Get_Selected_Feature_Example$$**$$Get_Closest_Point_Example$$**$$Find_Attribute_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
