---
title: "CustomSymbol::GetAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetAnnotation.htm"
---

# CustomSymbol::GetAnnotation

This method is obsolete and has been superseded
byBlockInstance::GetAnnotation.

Description

This method gets the general annotation object
for this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetAnnotation ( )

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the general annotation object |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->IGetAnnotation ( &retval
)

(Table)=========================================================

| Output: | (LPANNOTATION) retval | Pointer to the general annotation object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method gets the owning annotation object for
this custom symbol. The annotation object is a higher-level object which
contains methods that apply to all types of annotations (for example,
Annotation::SetPosition).

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
<param name="Items" value="CustomSymbol_Object$$**$$ZGetAnnotation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CustomSymbol\CustomSymbol__GetAnnotation.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
