---
title: "PartDoc::CreateFeatureFromBody2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__CreateFeatureFromBody2.htm"
---

# PartDoc::CreateFeatureFromBody2

This method is obsolete and has been superseded by[PartDoc::CreateFeatureFromBody3](sldworksAPI.chm::/PartDoc/PartDoc__CreateFeatureFromBody3.htm).

Description

This method creates a new feature from the
specified temporary body.

Syntax (OLE Automation)

retval = PartDoc.CreateFeatureFromBody2 ( pBody,
makeRefSurface)

(Table)=========================================================

| Input: | (LPDISPATCH) pBody | Dispatch pointer to the temporary body object |
| --- | --- | --- |
| Input: | (BOOL) makeRefSurface | If the body cannot be knitted to a solid or if
a solid body already exists in this model, then TRUE creates a reference
surface feature |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created
feature or NULL if the operation fails |

Syntax (COM)

status = PartDoc->ICreateFeatureFromBody2 ( pBody,
makeRefSurface, &retval )

(Table)=========================================================

| Input: | (LPBODY) pBody | Pointer to the temporary body object |
| --- | --- | --- |
| Input: | (BOOL) makeRefSurface | If the body cannot be knitted to a solid or if
a solid body already exists in this model, then TRUE creates a reference
surface feature |
| Output: | (LPFEATURE) retval | Pointer to a Dispatch object, the newly created
feature or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is intended to be the final call in a knitting operation.
The body that results from your knitting efforts, can be converted into
an imported body feature in the SolidWorks model. This is not limited
to Body objects obtained from knitting operations.

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
<param name="Items" value="PartDoc_Object$$**$$ZSewingRoutinesNEW$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\PartDoc\PartDoc__CreateFeatureFromBody2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
