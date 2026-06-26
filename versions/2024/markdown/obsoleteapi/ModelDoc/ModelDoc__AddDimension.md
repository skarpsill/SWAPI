---
title: "ModelDoc::AddDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddDimension.htm"
---

# ModelDoc::AddDimension

This
method is now Obsolete and has been superseded by[ModelDoc::AddDimension2](ModelDoc__AddDimension2.htm).

Description

This method creates a dimension for the current selected entities at
the specified location.

Syntax (OLE Automation)

retval = ModelDoc.AddDimension ( x,
y, z)

(Table)=========================================================

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Return: | (BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc->AddDimension
( x, y, z, &retval )

(Table)=========================================================

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Dimensions are created based on selection location. For example, creating
an angular dimension between two lines will get different results based
on which line endpoints are selected. Therefore, if you are using ModelDoc2::SelectByID
to select the entities for dimensioning, you should specify the XYZ selection
coordinates.

You must also leave the objectName argument empty, because if you pass
the objectName argument to ModelDoc2::SelectByID, then the selection routines
will try to locate that item withoutusing the coordinates. Because coordinates are ignored when an
objectName is passed, the dimensioning routines will not use a specific
selection location for the dimension. This will cause unpredictable results
in your dimension creation because you cannot be sure which line endpoint
is selected by the ModelDoc2::SelectByID routine.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$ZCreateDimension$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__AddDimension.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
