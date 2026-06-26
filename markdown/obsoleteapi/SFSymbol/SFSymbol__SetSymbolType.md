---
title: "SFSymbol::SetSymbolType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SFSymbol/SFSymbol__SetSymbolType.htm"
---

# SFSymbol::SetSymbolType

This method is obsolete and has been superseded
by[SFSymbol::SetSymbol](sldworksAPI.chm::/SFSymbol/SFSymbol__SetSymbol.htm).

Description

This method sets the symbol type for this surface-finish symbol.

Syntax (OLE Automation)

retval = SFSymbol.SetSymbolType (symbolType)

(Table)=========================================================

| Input: | (long) symbolType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the symbol type is successfully set,
FALSE if not |

Syntax (COM)

status = SFSymbol->SetSymbolType ( symbolType,
&retval )

(Table)=========================================================

| Input: | (long) symbolType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the symbol type is successfully set,
FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If an invalid symbol type is specified, the symbol
is not changed, and FALSE is returned.

To see the model or drawing changes caused by running
this method, you must redraw your window. See ModelDoc2::GraphicsRedraw2
for details.

To get the symbol type, use SFSymbol::GetSymbolType.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SFSymbol_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SFSymbol\SFSymbol__SetSymbolType.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
