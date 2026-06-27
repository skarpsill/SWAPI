---
title: "SelectionMgr::GetSelectedObject3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr_GetSelectedObject3.htm"
---

# SelectionMgr::GetSelectedObject3

This method is obsolete and has been superseded
by[SelectionMgr::GetSelectedObject4](SelectionMgr__GetSelectedObject4.htm).

Description

This method gets an interface to the currently selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObject3
( AtIndex)

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object as specified in Remarks or return NULL if type is not supported or if nothing is selected |

Syntax (COM)

status = SelectionMgr->IGetSelectedObject3
( AtIndex, &retval )

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPUNKNOWN) retval | Pointer to the selected object as specified in Remarks or return NULL if type is not supported or if nothing
is selected. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The following list includes all of the types supported
by this method as well as the object it returns for each type. You can
use SelectionMgr::GetSelectedObjectType2 to determineType
Selected.

(Table)=========================================================

| Type Selected | Object Returned | Notes |
| --- | --- | --- |
| swSelCOMPONENTS | Component |  |
| swSelDIMENSIONS | DisplayDimension | Use DisplayDimenion::GetDimension to get the Dimension object |
| swSelEDGES | Edge |  |
| swSelREFEDGES | Edge |  |
| swSelFACES | Face |  |
| swSelGTOLS | Gtol |  |
| swSelNOTES | Note |  |
| swSelSHEETS | Sheet |  |
| swSelSKETCHSEGS | SketchSegment |  |
| swSelEXTSKETCHSEGS | SketchSegment |  |
| swSelSKETCHPOINTS | SketchPoint |  |
| swSelEXTSKETCHPOINTS | SketchPoint |  |
| swSelVERTICES | Vertex |  |
| swSelDRAWINGVIEWS | View |  |
| swSelATTRIBUTES | Feature (see NOTE ) |  |
| swSelBODYFEATURES | Feature (see NOTE ) |  |
| swSelDATUMAXES | Feature (see NOTE ) |  |
| swSelDATUMPLANES | Feature (see NOTE ) |  |
| swSelDATUMPOINTS | Feature (see NOTE ) |  |
| swSelDETAILCIRCLES | Feature (see NOTE ) | Use Feature::GetSpecificFeature
to get the IDetailCircle |
| swSelMATES | Feature (see NOTE ) |  |
| swSelREFCURVES | Feature (see NOTE ) |  |
| swSelREFERENCECURVES | Feature (see NOTE ) |  |
| swSelREFSURFACES | Feature (see NOTE ) | Returns Feature object only when selection was made
in the FeatureManager design tree. Otherwise, a Face or Edge object is
returned. |
| swSelSECTIONLINES | Feature (see NOTE ) |  |
| swSelSKETCHES | Feature (see NOTE ) |  |
| swSelBOMS | BOM |  |
| swSelCENTERLINES | Centerline |  |
| swSelCTHREAD | Feature (see NOTE ) |  |
| NOTE: If the Object
Returned is a Feature object, then you must use Feature::GetSpecificFeature
if you want a more specific object interface. For example, if the selected
object is a Sketch, then SelectionMgr::GetSelectedObject3 returns a Feature
object. If you need the Sketch interface, then you must call the Feature::GetSpecificFeature
method to return the Sketch object. |  |  |

Not
Supported

swSelOLEITEMS

swSelCENTERMARKS

NOTE: When
reference surfaces are selected in the graphics view, this method returns
reference surface faces instead of the entire reference surface feature.
When dimensions are selected in the graphics view, this method returns
the DisplayDimension object instead of the Dimension object.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SelectionMgr_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SelectionMgr\SelectionMgr_GetSelectedObject3.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Change_Note_Text_Example$$**$$Find_Attribute_Example$$**$$Get_Assembly_Component_From_Selected_Entity_Example$$**$$Get_Closest_Point_Example$$**$$Get_Component_Face_By_Name_Example$$**$$Get_Selected_Feature_Example$$**$$Get_Vertex_Example$$**$$Object_Selection_and_Object_Naming_Example$$**$$Selections_Example$$**$$ZExample_Get__Curve_Spline_Points_Example_VB$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SelectionMgr\SelectionMgr_GetSelectedObject3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
