## SSH Keys

Generating SSH keys is like setting up a super secure passcode between your machine and whatever server you're planning to connect to, without the hassle of typing in passwords every time. This includes connecting WSL, to your cloud server (on DigitalOcean). But what is an SSH key? Well, it's a key that uses a `public key encryption` scheme.

### Public Key Encryption

Public key encryption is like having a special set of two keys: one for locking (public key) and another for unlocking (private key). You share the public key with everyone, but keep the private key to yourself. When someone wants to send you a secret message, they lock it using your public key. Once locked, the message can only be unlocked with your private key, ensuring that only you can read it. This way, secure communication is possible even over insecure channels.

## Generating SSH Keys

### RSA Key Generation
First up, RSA - the old guard of encryption. It's been around since the '70s but is still widely used due to its balance of security and compatibility. 

1. **Open your terminal**: Fire up your terminal app and make sure you're comfy with the command line. Zsh should greet you with its customizable prompt.

2. **Generate the RSA key pair**: Use the `ssh-keygen` command to start the key generation process. By default, it creates an RSA key, but you can specify the type and size for extra security. Here's how:

   ```zsh
   ssh-keygen -t rsa -b 4096
   ```

   Here, `-t rsa` specifies the type as RSA, and `-b 4096` cranks up the key size to 4096 bits, making it tougher to crack. RSA in considered insecure for block sizes of 1024 or less. Block sizes (key sizes) are not used in all SSH key generation schemes.

3. **Save the key**: `ssh-keygen` will ask where to save the new key. The default is usually fine (`~/.ssh/id_rsa`), but if you're juggling multiple keys, you might want to name it something more descriptive.

4. **Passphrase (Optional)**: It'll then prompt for a passphrase. Think of this as a key to your key — another layer of security. You can skip it, but adding one is a good practice.

5. **Public and Private Keys**: Once done, you'll have two files: one is your private key (`id_rsa`), and the other is the public key (`id_rsa.pub`). The public key is what you'll share with servers, while the private one is your secret.

### ED25519 Key Generation
Now, let's talk about ED25519. It's a newer kid on the block, known for its performance and security improvements over RSA. Use this one over the previous one (RSA).

1. **Generate the ED25519 key**: The process is similar to RSA, but you'll specify `ed25519` as the type:

   ```zsh
   ssh-keygen -t ed25519
   ```

2. **Follow the prompts**: Just like with RSA, you'll choose where to save it and whether to use a passphrase. ED25519 keys don't need a bit size specified since they have a fixed size that's optimized for security and performance.

### Why Use ED25519 Over RSA?
ED25519 keys are not only more secure but also faster due to their smaller size, making them ideal for modern applications. They're especially recommended for new SSH keys due to their resistance to certain types of cryptographic attacks that can affect RSA.

### Wrapping Up
After generating your keys, the next step is usually to copy your public key (`id_rsa.pub` or the ED25519 equivalent) to the servers you want to access with `ssh-copy-id user@hostname` or manually appending it to the `~/.ssh/authorized_keys` file on the server.

Generating SSH keys is a fundamental skill in securing your remote connections, and it's awesome you're incorporating stuff like this into your courses. Whether it's the tried-and-true RSA or the sleek, modern ED25519, each has its place in a well-rounded security toolkit.