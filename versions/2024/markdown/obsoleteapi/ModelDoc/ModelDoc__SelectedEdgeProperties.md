---
title: "ModelDoc::SelectedEdgeProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectedEdgeProperties.htm"
---

# ModelDoc::SelectedEdgeProperties

This method is obsolete
and has been superseded by[ModelDoc2::SelectedEdgeProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectedEdgeProperties.htm).

Description

This method sets the property values of the selected edge.

Syntax (OLE Automation)

retval = ModelDoc.SelectedEdgeProperties
( edgeName)

(Table)=========================================================

| Input: | (BSTR) edgeName | Name of the edge |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successfully changed the edge properties, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SelectedEdgeProperties
( edgeName, &retval )

(Table)=========================================================

| Input: | (BSTR) edgeName | Name of the edge |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully changed the edge properties, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If this edge does not already have a name, then this method sets the
name.

If the edge already has a name, then this method does not change the
name and returns FALSE. This behavior is intended to prevent a program
from renaming an edge that is referenced in some other location.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}name
to that edge. If you were to change that name, then there is no guarantee
that the mate will still be valid. Therefore, when using entity names,
you should first check to see if the entity is already named, and if so,
use the existing name. If no name exists for the edge, then you can give
the edge a name.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyFace$$**$$ZModifyNames$$**$$ZModifyEdge$$**$$ZSetNames$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SelectedEdgeProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
