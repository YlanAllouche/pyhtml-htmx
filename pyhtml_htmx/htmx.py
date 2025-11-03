from typing import Literal, NotRequired, TypedDict, cast

HxSwapValue = Literal[
    "innerHTML",
    "outerHTML",
    "textContent",
    "beforebegin",
    "afterbegin",
    "beforeend",
    "afterend",
    "delete",
    "none",
]


class HxAttrs(TypedDict, total=False):
    """TypedDict for HTMX attributes with type checking.

    This ensures type checkers understand that all keys start with 'hx_',
    preventing false conflicts with standard HTML attributes like 'target'.
    """

    hx_boost: NotRequired[str]
    hx_confirm: NotRequired[str]
    hx_delete: NotRequired[str]
    hx_disable: NotRequired[str]
    hx_disabled_elt: NotRequired[str]
    hx_disinherit: NotRequired[str]
    hx_encoding: NotRequired[str]
    hx_ext: NotRequired[str]
    hx_get: NotRequired[str]
    hx_headers: NotRequired[str]
    hx_history: NotRequired[str]
    hx_history_elt: NotRequired[str]
    hx_include: NotRequired[str]
    hx_indicator: NotRequired[str]
    hx_inherit: NotRequired[str]
    hx_on: NotRequired[str]
    hx_params: NotRequired[str]
    hx_patch: NotRequired[str]
    hx_post: NotRequired[str]
    hx_preserve: NotRequired[str]
    hx_prompt: NotRequired[str]
    hx_push_url: NotRequired[str]
    hx_put: NotRequired[str]
    hx_replace_url: NotRequired[str]
    hx_request: NotRequired[str]
    hx_select: NotRequired[str]
    hx_select_oob: NotRequired[str]
    hx_swap: NotRequired[str]
    hx_swap_oob: NotRequired[str]
    hx_sync: NotRequired[str]
    hx_target: NotRequired[str]
    hx_trigger: NotRequired[str]
    hx_validate: NotRequired[str]
    hx_vals: NotRequired[str]
    hx_vars: NotRequired[str]


def hx(
    boost: str | bool | None = None,
    confirm: str | None = None,
    delete: str | None = None,
    disable: bool | None = None,
    disabled_elt: str | None = None,
    disinherit: str | None = None,
    encoding: str | None = None,
    ext: str | None = None,
    get: str | None = None,
    headers: str | None = None,
    history: bool | None = None,
    history_elt: bool | None = None,
    include: str | None = None,
    indicator: str | None = None,
    inherit: str | None = None,
    on: str | None = None,
    params: str | None = None,
    patch: str | None = None,
    post: str | None = None,
    preserve: bool | None = None,
    prompt: str | None = None,
    push_url: str | bool | None = None,
    put: str | None = None,
    replace_url: str | bool | None = None,
    request: str | None = None,
    select: str | None = None,
    select_oob: str | None = None,
    swap: HxSwapValue | None = None,
    swap_oob: str | bool | None = None,
    sync: str | None = None,
    target: str | None = None,
    trigger: str | None = None,
    validate: bool | None = None,
    vals: str | None = None,
    vars: str | None = None,
) -> dict[str, str | bool]:
    """Create a dictionary of HTMX attributes for use as PyHTML tags.

    This function provides a clean reference to HTMX attributes without the `hx_` prefix.
    Use the `**` operator to spread the returned dictionary into any PyHTML tag.

    Args:
        boost: Boost normal anchors and forms to use AJAX instead. For anchors, clicking
            issues a GET request to the URL in `href` and pushes the URL to history. The
            target is `<body>` and swap strategy is `innerHTML` by default.
            Example: boost=True or boost="true"
            See: https://htmx.org/attributes/hx-boost/

        confirm: Show a confirmation dialog before issuing a request. Useful for
            destructive actions to ensure the user wants to proceed.
            Example: confirm="Are you sure you wish to delete your account?"
            See: https://htmx.org/attributes/hx-confirm/

        delete: Issue a DELETE request to the specified URL and swap the HTML into the DOM.
            Example: delete="/account"
            See: https://htmx.org/attributes/hx-delete/

        disable: Disable htmx processing for this element and all its children. Useful as
            a backup for HTML escaping with user-generated content to prevent malicious
            scripting attacks. The value is ignored and cannot be reversed by children.
            Example: disable=True
            See: https://htmx.org/attributes/hx-disable/

        disabled_elt: CSS selector of elements that will have the `disabled` attribute
            added for the duration of the request. Can be 'this', 'closest <selector>',
            'find <selector>', 'next', 'next <selector>', 'previous', 'previous <selector>'.
            Example: disabled_elt="this" or disabled_elt="closest fieldset"
            See: https://htmx.org/attributes/hx-disabled-elt/

        disinherit: Control automatic attribute inheritance. By default, attributes like
            hx-target inherit from parent elements. Use this to prevent inheritance in
            specific parts of the page.
            Example: disinherit="*" or disinherit="hx-target hx-swap"
            See: https://htmx.org/attributes/hx-disinherit/

        encoding: Switch request encoding from `application/x-www-form-urlencoded` to
            `multipart/form-data`, usually to support file uploads in AJAX requests.
            Example: encoding="multipart/form-data"
            See: https://htmx.org/attributes/hx-encoding/

        ext: Enable htmx extensions for this element and all its children. Value can be
            a single extension name or comma-separated list of extensions.
            Example: ext="json-enc" or ext="json-enc,morph"
            See: https://htmx.org/attributes/hx-ext/

        get: Issue a GET request to the specified URL and swap the HTML into the DOM.
            Example: get="/example"
            See: https://htmx.org/attributes/hx-get/

        headers: Add headers to the AJAX request. Value is a JSON object of name-value pairs.
            Example: headers='{"X-Custom-Header": "value"}'
            See: https://htmx.org/attributes/hx-headers/

        history: Set to False to prevent sensitive data being saved to localStorage when
            htmx snapshots page state. History navigation works normally but restoration
            requests content from server instead of cache.
            Example: history=False
            See: https://htmx.org/attributes/hx-history/

        history_elt: Specify the element used to snapshot and restore page state during
            navigation. Defaults to `<body>`. Element must always be visible or history
            navigation won't work properly.
            Example: history_elt=True
            See: https://htmx.org/attributes/hx-history-elt/

        include: CSS selector of additional elements to include in the AJAX request.
            Can be 'this', 'closest <selector>', 'find <selector>', 'next <selector>',
            or 'previous <selector>'.
            Example: include="#extra-data" or include="closest form"
            See: https://htmx.org/attributes/hx-include/

        indicator: CSS selector of the element that will have the `htmx-request` class
            added during the request. Use this to show spinners or progress indicators.
            Example: indicator="#spinner" or indicator="closest .loading"
            See: https://htmx.org/attributes/hx-indicator/

        inherit: Explicitly specify attribute inheritance when `htmx.config.disableInheritance`
            is set to true. Lists which attributes should inherit from parent elements.
            Example: inherit="hx-target hx-swap"
            See: https://htmx.org/attributes/hx-inherit/

        on: Embed inline scripts to respond to events directly on the element. Similar to
            onevent properties like onClick but handles any JavaScript event including htmx events.
            Example: on="htmx:afterRequest: console.log('Done!')"
            See: https://htmx.org/attributes/hx-on/

        params: Filter parameters submitted with the AJAX request. Values: '*' (all, default),
            'none' (no parameters), 'not <param-list>' (all except listed), '<param-list>' (only listed).
            Example: params="*" or params="not password"
            See: https://htmx.org/attributes/hx-params/

        patch: Issue a PATCH request to the specified URL and swap the HTML into the DOM.
            Example: patch="/account"
            See: https://htmx.org/attributes/hx-patch/

        post: Issue a POST request to the specified URL and swap the HTML into the DOM.
            Example: post="/account/enable"
            See: https://htmx.org/attributes/hx-post/

        preserve: Keep this element unchanged during HTML replacement. Elements are preserved
            by id when htmx updates any ancestor element. Must have an unchanging id.
            Example: preserve=True
            See: https://htmx.org/attributes/hx-preserve/

        prompt: Show a prompt before issuing a request. The prompt value is included in
            the request in the HX-Prompt header.
            Example: prompt="Enter your account name to confirm deletion"
            See: https://htmx.org/attributes/hx-prompt/

        push_url: Push a URL into browser location history, creating a new history entry
            for browser back/forward navigation. htmx snapshots the current DOM and saves
            it to history cache. Values: True (pushes fetched URL), False (disables pushing),
            or a URL string (relative or absolute).
            Example: push_url=True or push_url="/new-url"
            See: https://htmx.org/attributes/hx-push-url/

        put: Issue a PUT request to the specified URL and swap the HTML into the DOM.
            Example: put="/account"
            See: https://htmx.org/attributes/hx-put/

        replace_url: Replace the current URL in browser location history. Values: True
            (replaces with fetched URL), False (disables replacement), or a URL string
            (relative or absolute).
            Example: replace_url=True or replace_url="/updated-url"
            See: https://htmx.org/attributes/hx-replace-url/

        request: Configure request aspects via JSON-like syntax. Available: 'timeout'
            (milliseconds), 'credentials' (send credentials), 'noHeaders' (strip all headers).
            Example: request='{"timeout":100}'
            See: https://htmx.org/attributes/hx-request/

        select: CSS selector to select specific content from the response to swap.
            Example: select="#info-detail"
            See: https://htmx.org/attributes/hx-select/

        select_oob: CSS selector of content from response for out-of-band swaps. Value is
            comma-separated list of elements. Almost always paired with `select`.
            Example: select_oob="#alert"
            See: https://htmx.org/attributes/hx-select-oob/

        swap: How the response will be swapped relative to the target. Options: 'innerHTML'
            (replace inner HTML, default), 'outerHTML' (replace entire element), 'textContent'
            (replace text only), 'beforebegin' (insert before element), 'afterbegin' (insert
            as first child), 'beforeend' (insert as last child), 'afterend' (insert after element),
            'delete' (delete element), 'none' (don't swap, but process out-of-band items).
            Example: swap="outerHTML" or swap="beforeend"
            See: https://htmx.org/attributes/hx-swap/

        swap_oob: Mark element for out-of-band swapping, allowing updates to elements other
            than the target. Enables piggybacking updates on a response.
            Example: swap_oob=True or swap_oob="true"
            See: https://htmx.org/attributes/hx-swap-oob/

        sync: Synchronize AJAX requests between multiple elements. Format: CSS selector
            followed by optional strategy. Strategies: 'drop' (ignore if request in flight),
            'abort' (abort if another request occurs), 'replace' (abort current and replace
            with this), 'queue' (queue this request).
            Example: sync="this:drop" or sync="form:abort"
            See: https://htmx.org/attributes/hx-sync/

        target: CSS selector of the element to swap content into (instead of the element
            issuing the request). Can be 'this', 'closest <selector>', 'find <selector>',
            'next', 'next <selector>', 'previous', or 'previous <selector>'.
            Example: target="#result" or target="closest .container"
            See: https://htmx.org/attributes/hx-target/

        trigger: Event that triggers the AJAX request. Can be an event name with optional
            filters and modifiers, a polling definition ('every <timing>'), or comma-separated list.
            Example: trigger="click" or trigger="keyup changed delay:500ms"
            See: https://htmx.org/attributes/hx-trigger/

        validate: Force element to validate via HTML5 Validation API before submitting request.
            Only forms validate by default. Adding validate=True to input, textarea, or select
            enables validation before requests.
            Example: validate=True
            See: https://htmx.org/attributes/hx-validate/

        vals: Add to parameters submitted with the AJAX request. Value is a JSON object
            of name-value pairs.
            Example: vals='{"extra": "data"}'
            See: https://htmx.org/attributes/hx-vals/

        vars: DEPRECATED - Use `vals` instead. Dynamically add to parameters submitted
            with AJAX request.
            Example: vars='extraData'
            See: https://htmx.org/attributes/hx-vars/

    Returns:
        Dictionary of HTMX attributes with `hx_` prefix, ready to spread into PyHTML
        tags using `**hx(...)`. Boolean values are converted to lowercase strings
        ("true"/"false") for HTML compatibility.

    Example:
        Basic GET request:
        >>> import pyhtml as p
        >>> from pyhtml_htmx import hx
        >>> button = p.button("Load Data", **hx(get="/api/data"))
        >>> str(button)
        '<button hx-get="/api/data">Load Data</button>'

        With target and swap:
        >>> button = p.button(
        ...     "Update",
        ...     **hx(post="/api/update", target="#content", swap="innerHTML")
        ... )
        >>> str(button)
        '<button hx-post="/api/update" hx-target="#content" hx-swap="innerHTML">Update</button>'

        Debounced search input:
        >>> search = p.input_(
        ...     type="search",
        ...     placeholder="Search...",
        ...     **hx(
        ...         post="/search",
        ...         trigger="keyup changed delay:500ms",
        ...         target="#results"
        ...     )
        ... )

        With loading indicator:
        >>> button = p.button(
        ...     "Save",
        ...     **hx(
        ...         post="/save",
        ...         indicator="#spinner",
        ...         disabled_elt="this"
        ...     )
        ... )

    Note:
        All parameters use clean names without the `hx_` prefix. The function adds
        the prefix internally before returning. This makes the API more intuitive:
        `hx(get="/url")` instead of `hx(hx_get="/url")`.

    See Also:
        https://htmx.org/reference/ - Official HTMX attributes reference
        https://htmx.org/docs/ - HTMX documentation
    """

    def _to_str(value: str | bool) -> str:
        """Convert boolean values to lowercase string for HTML compatibility."""
        if isinstance(value, bool):
            return "true" if value else "false"
        return value

    # attrs: HxAttrs = {}
    attrs = {}

    if boost is not None:
        attrs["hx_boost"] = _to_str(boost)
    if confirm is not None:
        attrs["hx_confirm"] = confirm
    if delete is not None:
        attrs["hx_delete"] = delete
    if disable is not None:
        attrs["hx_disable"] = _to_str(disable)
    if disabled_elt is not None:
        attrs["hx_disabled_elt"] = disabled_elt
    if disinherit is not None:
        attrs["hx_disinherit"] = disinherit
    if encoding is not None:
        attrs["hx_encoding"] = encoding
    if ext is not None:
        attrs["hx_ext"] = ext
    if get is not None:
        attrs["hx_get"] = get
    if headers is not None:
        attrs["hx_headers"] = headers
    if history is not None:
        attrs["hx_history"] = _to_str(history)
    if history_elt is not None:
        attrs["hx_history_elt"] = _to_str(history_elt)
    if include is not None:
        attrs["hx_include"] = include
    if indicator is not None:
        attrs["hx_indicator"] = indicator
    if inherit is not None:
        attrs["hx_inherit"] = inherit
    if on is not None:
        attrs["hx_on"] = on
    if params is not None:
        attrs["hx_params"] = params
    if patch is not None:
        attrs["hx_patch"] = patch
    if post is not None:
        attrs["hx_post"] = post
    if preserve is not None:
        attrs["hx_preserve"] = _to_str(preserve)
    if prompt is not None:
        attrs["hx_prompt"] = prompt
    if push_url is not None:
        attrs["hx_push_url"] = _to_str(push_url)
    if put is not None:
        attrs["hx_put"] = put
    if replace_url is not None:
        attrs["hx_replace_url"] = _to_str(replace_url)
    if request is not None:
        attrs["hx_request"] = request
    if select is not None:
        attrs["hx_select"] = select
    if select_oob is not None:
        attrs["hx_select_oob"] = select_oob
    if swap is not None:
        attrs["hx_swap"] = swap
    if swap_oob is not None:
        attrs["hx_swap_oob"] = _to_str(swap_oob)
    if sync is not None:
        attrs["hx_sync"] = sync
    if target is not None:
        attrs["hx_target"] = target
    if trigger is not None:
        attrs["hx_trigger"] = trigger
    if validate is not None:
        attrs["hx_validate"] = _to_str(validate)
    if vals is not None:
        attrs["hx_vals"] = vals
    if vars is not None:
        attrs["hx_vars"] = vars

    return attrs


htmx = hx
