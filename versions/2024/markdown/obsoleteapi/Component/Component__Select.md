---
title: "Component::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__Select.htm"
---

# Component::Select

This method is obsolete and has been superseded by[Component2::Select](../Component2/Component2__Select.htm).

Description

This method selects the component and either
appends it to the selections or replaces the entire selection list.

Syntax (OLE Automation)

retval = Component.Select ( appendFlag )

(Table)=========================================================

| Input: | (BOOL) appendFlag | TRUE appends the current selection list, FALSE replaces the selection
list |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the feature was selected, FALSE if it was not |

Syntax (COM)

status = Component->Select ( appendFlag, &retval
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the current selection list, FALSE replaces the selection
list |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the feature was selected, FALSE if it was not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name=Items value="ZReleaseNotes2001$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Component\Component__Select.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name=Items value="Component_Object$$**$$ZGetSelection$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Component\Component__Select.htm" >
<param name=_ID value="RelatedTopic1" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
