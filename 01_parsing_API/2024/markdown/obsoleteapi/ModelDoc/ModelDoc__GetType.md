---
title: "ModelDoc::GetType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetType.htm"
---

# ModelDoc::GetType

This method is obsolete and has been superseded
by[ModelDoc2::GetType](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetType.htm).

Description

This method returns the type of the document.

Syntax (OLE Automation)

retval = ModelDoc.GetType ()

(Table)=========================================================

| Return: | (long) retval | Type of document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetType ( &retval
)

(Table)=========================================================

| Output: | (long) retval | Type of document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The document type can be one of the following values:

swDocNONE- no document

swDocPART- part document

swDocASSEMBLY-
assembly document

swDocDRAWING- drawing document

These definitions replace these now obsolete types:

TYPE_PART= 1

TYPE_ASSEMBLY= 2

TYPE_DRAWING= 3

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoModelDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetType.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Enumerate_Bodies_Example$$**$$Get_All_Edges_and_Vertices_Example$$**$$Get_Closest_Point_Example$$**$$Get_Drawing_View_Transform_Example$$**$$Get_Model_Info_Example$$**$$Get_ModelView_Screen_Transform_Example$$**$$Highlight_Face_Example$$**$$Note_Creation_Example$$**$$Set_Drawing_View_Display_Example$$**$$ZExample_Get_Excel_Cell_Value_for_Density_VB$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetType.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
