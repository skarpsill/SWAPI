---
title: "ModelDoc::ReattachOrdinate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ReattachOrdinate.htm"
---

# ModelDoc::ReattachOrdinate

This method is obsolete
and has been superseded by[ModelDoc2::ReattachOrdinate](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ReattachOrdinate.htm).

Description

This method reattaches an ordinate dimension
to a different entity.

Syntax (OLE Automation)

retval = ModelDoc.ReattachOrdinate ( )

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if the reattachment was successful, FALSE
otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->ReattachOrdinate ( &retval
)

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if the reattachment was successful, FALSE
otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

To use this method, you must first select the dimension
to be reattached and then call ModelDoc::AndSelecteByID to select the
new entity to which to attach this dimension. For example:

Part.SelectByID "D6@Sketch2@Part1.SLDDRW", "DIMENSION",
0.0194564, 0.0695452, 0

Part.AndSelectByID "", "EDGE", 0.0310388,
0.05887719999651, -499.8885

Part.ReAttachOrdinate

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__ReattachOrdinate.htm" >
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__ReattachOrdinate.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
