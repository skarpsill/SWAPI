---
title: "Body::CreateBlendSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBlendSurface.htm"
---

# Body::CreateBlendSurface

This method is obsolete and has been superseded by[Body2::CreateBlendSurface](sldworksAPI.chm::/Body2/Body2__CreateBlendSurface.htm).

Description

This method creates a constant radius rolling ball blend surface (also
known as a pipe surface) between two side surfaces. The surface generated
is the path traced out when a sphere of the blend radius is rolled in
contact with the two side surfaces. The center of the sphere rolls along
the spine, which is the intersection of these two surfaces when offset
by the blend radius.

Syntax (OLE Automation)

retval = Body.CreateBlendSurface
( Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec,
HaveHelpBox, HelpBox)

(Table)=========================================================

| Input: | (LPDISPATCH) Surface1 | Dispatch pointer to the first side surface |
| --- | --- | --- |
| Input: | (double) Range1 | Signed offset of Surface1 |
| Input: | (LPDISPATCH) Surface2 | Dispatch pointer to the second side surface |
| Input: | (double) Range2 | Signed offset of Surface2 |
| Input: | (VARIANT) StartVec | VARIANT of type SafeArray of 3 doubles representing a point close to
the tart of the blend spine |
| Input: | (VARIANT) EndVec | VARIANT of type SafeArray of 3 doubles representing a point close to
the end of the blend spine |
| Input: | (int) HaveHelpVec | Optional boolean if help vector is provided |
| Input: | (VARIANT) HelpVec | VARIANT of type SafeArray of 3 doubles representing the direction of
the Help vector |
| Input: | (int) HaveHelpBox | Optional Boolean if box is provided |
| Input: | (VARIANT) HelpBox | VARIANT of type SafeArray of 6 doubles bounding the area of interest |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created surface |

Syntax
(COM)

status = Body->ICreateBlendSurface
( Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec,
HaveHelpBox, HelpBox, &retval )

(Table)=========================================================

| Input: | (LPSURFACE) Surface1 | Pointer to the first side surface |
| --- | --- | --- |
| Input: | (double) Range1 | Signed offset of Surface1 |
| Input: | (LPSURFACE) Surface2 | Pointer to the second side surface |
| Input: | (double) Range2 | Signed offset of Surface2 |
| Input: | (double*) StartVec | Array of 3 doubles representing a point close to the start of the blend
spine |
| Input: | (double*) EndVec | Array of 3 doubles representing a point close to the end of the blend
spine |
| Input: | (int) HaveHelpVec | Optional Boolean if help vector is provided |
| Input: | (double*) HelpVec | Array of 3 doubles representing the direction of the Help vector. |
| Input: | (int) HaveHelpBox | Optional boolean if box is provided |
| Input: | (double*) HelpBox | Array of 6 doubles bounding the area of interest |
| Output: | (LPSURFACE) retval | Pointer to the newly created surface. |
| Return: | (HRESULT)status | S_OK if successful |

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZCreateSurface$$**$$ZAccessorByCreate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateBlendSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
