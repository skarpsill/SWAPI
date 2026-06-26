---
title: "ModelDoc::AndSelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AndSelectByID.htm"
---

# ModelDoc::AndSelectByID

This
method is obsolete and has been superseded by[ModelDoc2::AndSelectByID](../ModelDoc2/ModelDoc2__AndSelectByID.htm).

Description

This method adds an object to the list of selected items, or removes
it if it is already selected. For a full description of selection and
the arguments, see ModelDoc::SelectByID.

Syntax (OLE Automation)

retval = ModelDoc.AndSelectByID ( selID,
selParams, x, y, z)

(Table)=========================================================

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Y selection location |
| Input: | (double) z | Z selection location |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->AndSelectByID
( selID, selParams, x, y, z, &retval )

(Table)=========================================================

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Y selection location |
| Input: | (double) z | Z selection location |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For more details, refer to the ModelDoc::SelectByID
documentation.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name=_Version value="65536" >
<param name=_ExtentX value="26" >
<param name=_ExtentY value="26" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$ZGetSelection$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__AndSelectByID.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
