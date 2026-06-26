---
title: "Body::CreateBoundedSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBoundedSurface.htm"
---

# Body::CreateBoundedSurface

This
method is obsolete and has been superseded by[Body2::CreateBoundedSurface](sldworksAPI.chm::/Body2/Body2__CreateBoundedSurface.htm).

Description

This method creates a bounded surface from an independent base surface.

Syntax (OLE Automation)

retval
= Body.CreateBoundedSurface ( uOpt, vOpt, uvParams)

(Table)=========================================================

| Input: | (BOOL)
uOpt | TRUE
if the U parameter range is given in uvData, FALSE if the entire U parameter
range is used |
| --- | --- | --- |
| Input: | (BOOL)
vOpt | TRUE
if the V parameter range is given in uvData, FALSE if the entire V parameter
range is used |
| Input: | (VARIANT)
uvParams | VARIANT
of type SafeArray of 4 doubles |
| Return: | (BOOL)
retval | TRUE
if bounded surface creation was successful, FALSE if it was not |

Syntax (COM)

status
= Body->ICreateBoundedSurface ( UOpt, VOpt, UVParams )

(Table)=========================================================

| Input: | (VARIANT_BOOL)
UOpt | TRUE
if the U parameter range is given in uvData, FALSE if the entire U parameter
range is used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL)
VOpt | TRUE
if the V parameter range is given in uvData, FALSE if the entire V parameter
range is used |
| Input: | (double*)
UVParams | An
array of 4 doubles |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

Before you call this method, youmust call one of the base surface creation methods, such as Body::CreateBsplineSurface.

The UOpt and VOpt arguments allow the you to supply
parameter range information so that you can create a bounded surface from
part of the base surface. If both uOpt and vOpt are set to FALSE, then
SolidWorks uses the entire parameter ranges. SolidWorks cannot do this
for surfaces with infinite parameter ranges.

UVParams contains 4 doubles describing
the UV parameter ranges.

- U parameter range is
  supplied in uvData[0] and uvData[1]. UvData[0] must be less than uvData[1].
- V parameter range is
  supplied in uvData[2] and uvData[3]. UvData[2] must be less than uvData[3].

If you want to construct a solid body from bounded
surfaces, then you must first call PartDoc::CreateNewBody, which arranges
for a placeholder for this bounded surface.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZCreateSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateBoundedSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
