Vue.component('comment', {
    props: {
        author: String,
    },
    template: `
            <div class="comment">
                <b v-if="!!author">{{author}}</b>
                <slot/>
            </div>
            `,
});

Vue.component('addComment', {
    template: `
        <div ref="commentForm" class="comment">
            <div><b>Add new comment</b></div>
            <input v-model="user" placeholder="User name" type="text" name="new-comment__user"><br>
            <input v-model="text" placeholder="Your Comment" type="text" name="new-comment__text">
            <button @click="this.submit">Submit</button>
            <div v-if="errorMessage" style="color: red">{{errorMessage}}</div>
        </div> 
    `,
    data() {
        return {
            user: undefined,
            text: undefined,
            errorMessage: undefined
        }
    },
    methods: {
        submit: function (e) {
            e.preventDefault();

            const payload = {
                user: this.user,
                text: this.text,
                book: Number(book_id),
            };

            axios({
                url: "",
                method: "POST",
                headers: {
                    type: 'application/json',
                    'X-Requested-With': 'XMLHttpRequest', // This must be here for Django to evaluate is_ajax() to True.
                    "X-CSRFTOKEN": csrf_token,
                },
                data: payload,
            })
                .then(res => {
                    console.log("Request was sent successfully", res.data)
                    this.$emit('success', res.data)
                })
                .catch(err => {
                    console.log(err.response.data.error);
                    this.errorMessage = err.response.data.error;
                })
        }


    }

});

new Vue({
    el: '#dynamic_comments', // Element with this id will be found in the DOM and the content of it will be rendered by Vue.js during runtime.
    components: ['addComment', 'comment'],
    template: `
                <div>
                    <comment v-for="(comment, i) in comments" :key="i" :author="comment.user">{{ comment.text }}</comment>  
                    <addComment @success="appendComment" />   
                </div>     
            `,
    data: {
        comments: []
    },
    methods: {
        appendComment(comment) {
            this.comments.push(comment)
        }
    }
});

