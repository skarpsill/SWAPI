---
title: "CustomSymbol::SetText"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__SetText.htm"
---

# CustomSymbol::SetText

This
method is obsolete and has been superseded by CustomSymbol::GetNotesCount and CustomSymbol::GetNotes .

Description

This method sets one of the text strings in
this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.SetText (index,
text)

(Table)=========================================================

| Input: | (long) index | Zero-based index of the string to be replaced
by the text |
| --- | --- | --- |
| Input: | (BSTR) text | Text string |
| Return: | (BOOL) retval | TRUE if text was set successfully, FALSE if not |

Syntax (COM)

status = CustomSymbol->SetText ( index, text,
&retval )

(Table)=========================================================

| Input: | (long) index | Zero-based index of the string to be replaced
by the text |
| --- | --- | --- |
| Input: | (BSTR) text | Text string |
| Output: | (VARIANT_BOOL) retval | TRUE if text was set successfully, FALSE if not |
| Return: | (HRESULT) retval | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="CustomSymbol_Object$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\CustomSymbol\CustomSymbol__SetText.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
